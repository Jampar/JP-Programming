// GeneAnalysis.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h" 
#include "GeneAnalysisHeader.h"
#include <list>
#include <iostream>
#include <time.h>
#include <string>

using namespace std;

clock_t t_start = clock();

string sequence_path = "D:/Documents/C++ Projects/GeneAnalysis/GeneAnalysis/S cerevisiae Chr 4.gb";

list<string> gene_extracts;

const int width = 4;
const int height = 200;
int search_bound[] = { 150,50 };

void Analyse(string sequence_path)
{
	FASTAFilter f_filter;

	f_filter.width = width;
	f_filter.height = height;
	f_filter.search_bound[0]= search_bound[0];
	f_filter.search_bound[1] = search_bound[1];

	string sequence = f_filter.FindGeneSequence(sequence_path);
	list<string> gene_lines = f_filter.FindGeneLines(sequence_path);

	string gene_line;

	list<string>::iterator it;
	for (it = gene_lines.begin(); it != gene_lines.end(); ++it) {
		gene_extracts.push_back(f_filter.FindSequenceExtract(*it, sequence));
	}

	int freq_array [width][height];
	f_filter.PopulateBaseFrequency(gene_extracts, freq_array);

	string files[4]{ "","","","" };

	f_filter.CreateDataFiles(freq_array, files);

	printf("Time taken: %.2fs\n", (double)(clock() - t_start) / CLOCKS_PER_SEC);

	GraphPlotter gp;
	gp.PlotDataFiles(files);
	
}


// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
