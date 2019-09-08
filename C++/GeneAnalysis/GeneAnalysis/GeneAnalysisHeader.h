#pragma once

#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <stdio.h>     
#include <cctype>
#include <algorithm>
#include "D:/Documents/gnuplot_header/gnuplot.h"

using namespace std;

class FASTAFilter {

	public:
		int width = 4;
		int height = 200;
		int search_bound[2];

		//Finds all the line numbers of the lines in the file that the lookup word is on.
		list<string> FindGeneLines(string sequence_path) {

			cout << "Finding gene lookup lines..." << '\n';

			string lookup = " gene ";

			//List holding all line numbers that have the word on.
			list<string> lines;

			//Each line of the file.
			string line;

			// Open filestream.
			ifstream ifs(sequence_path);

			//While the filestream has not reached the end of file.
			while (!ifs.eof())
			{
				//Get each line and put it in the line variable.
				getline(ifs, line);

				//search returns a position on the line if found or std::string::npos if not.
				string::size_type search = line.find(lookup);

				//if the word is found add the line number to the list.
				if (search != string::npos && search < 11) {
					line.erase(0, 21);
					lines.push_back(line);
				}
			}
			ifs.close();

			cout << "Found gene lookup lines." << '\n';

			return lines;
		}

		string FindGeneSequence(string sequence_path) {

			string start_lookup = "ORIGIN";
			string end_lookup = "//";

			int sequence_bounds[2];

			// Open filestream
			ifstream bounds_ifs(sequence_path);

			//Holds the line info
			string line;

			//iterator variable.
			int i = 1;

			cout << "Finding gene sequence..." << '\n';

			//While the filestream has not reached the end of file
			while (!bounds_ifs.eof())
			{
				//Get each line and put it in the line variable
				getline(bounds_ifs, line);

				//search returns a position on the line if found or std::string::npos if not.
				string::size_type start_search_line = line.find(start_lookup);

				//if the lookup is found add the line number to the list.
				if (start_search_line != string::npos && start_search_line < 7) {
					sequence_bounds[0] = i + 1;
				}

				//search returns a position on the line if found or std::string::npos if not.
				string::size_type end_search_line = line.find(end_lookup);

				//if the lookup is found add the line number to the list.
				if (end_search_line != string::npos && end_search_line < 3) {
					sequence_bounds[1] = i - 1;
				}

				i++;
			}
			bounds_ifs.close();


			i = 1;

			// Open filestream
			ifstream seq_ifs(sequence_path);

			bool start_reading = false;

			string seq;
			//While the filestream has not reached the end of file
			while (!seq_ifs.eof())
			{
				if (i == sequence_bounds[0]) start_reading = true;
				if (i == sequence_bounds[1]) start_reading = false;

				//Get each line and put it in the line variable
				getline(seq_ifs, line);

				if (start_reading) {

					line.erase(0, 10);

					for (int c = 0; c < line.length()+1; c++) {
						if (line[c] == ' ') {
							line.erase(c, 1);
						}
					}
					seq += line;
				}

				i++;
			}
			cout << "Found gene sequence." << '\n';

			return seq;
		}

		string FindSequenceExtract(string gene_line, string sequence) {

			int nums[2];
			bool start_number = false;
			bool first_number = true;
			string num_str;
			int gene_start;

			bool complement = false;

			if (gene_line[0] == 'c') {
				complement = true;
			}

			for (int c = 0; c < gene_line.length() + 1; c++) {

				if (std::isdigit(gene_line[c])) {
					if (start_number == false) {
						start_number = true;
						num_str = "";
					}
					num_str.append(std::string(1, gene_line[c]));
				}
				else {
					if (start_number == true) {

						start_number = false;

						if (first_number) {
							nums[0] = stoi(num_str);
						}
						else {
							nums[1] = stoi(num_str);

						}
						first_number = false;
					}
				}
			}
			string gene_extract;

			if (complement) {
				gene_start = nums[1];


				//find complement sequence.
				for (int s = gene_start + search_bound[0] - 1; s > gene_start - search_bound[1] - 2; s--) {

					char base = sequence[s];

					if (sequence[s] == 'a') base = 't';
					if (sequence[s] == 'g') base = 'c';
					if (sequence[s] == 'c') base = 'g';
					if (sequence[s] == 't') base = 'a';

					gene_extract += base;
				}
			}
			else {
				gene_start = nums[0];

				for (int s = gene_start - search_bound[0] - 1; s < gene_start + search_bound[1] + 1; s++) {
					char base = sequence[s];

					gene_extract += base;
				}
			}
			return gene_extract;
		}

		void PopulateBaseFrequency(list<string> extracts, int(&arr)[4][200]) {

			for (int j = 0; j < 200; j++) {
					arr[0][j] = 0;
					arr[1][j] = 0;
					arr[2][j] = 0;
					arr[3][j] = 0;
			}
			

			for (string line : extracts) {
				int i = 0;
				for (char character : line) {
					if (i < 200) {
						if (character == 'a')
							arr[0][i] += 1;

						if (character == 'g')
							arr[1][i] += 1;

						if (character == 'c')
							arr[2][i] += 1;

						if (character == 't')
							arr[3][i] += 1;

						i++;
					}
					else {
						break;
					}
				}
			}
		}

		void CreateDataFiles(int(&freq_array)[4][200],string* files) {

			for (int g = 0; g < 4; g++) {

				string base_symbol;

				if (g == 0) base_symbol = 'A';
				if (g == 1) base_symbol = 'G';
				if (g == 2) base_symbol = 'C';
				if (g == 3) base_symbol = 'T';

				string data_path = "Data/";
				string file_ext = ".dat";
				string	file_name = data_path + "freq" + base_symbol + file_ext;

				files[g] = file_name;

				ofstream outfile(file_name);

				if (outfile.good()) {

					outfile << "#pos		" << "freq		" << '\n';

					for (int x = 0; x < height; x++) {
						outfile << x << "		" << freq_array[g][x] << '\n';
					}
				}

				outfile.close();
			}
		}

};

class GraphPlotter {
	public:
		void PlotDataFiles(string* data_paths) {

		GnuplotPipe gp;

		string sgle_qts = "'";
		string sent_line = "plot " + sgle_qts + data_paths[0] + sgle_qts + ',' + sgle_qts + data_paths[1] + sgle_qts + ',' + sgle_qts + data_paths[2] + sgle_qts + ',' + sgle_qts + data_paths[3] + sgle_qts;

		gp.sendLine("set style data lines");
		gp.sendLine(sent_line);
	}
};