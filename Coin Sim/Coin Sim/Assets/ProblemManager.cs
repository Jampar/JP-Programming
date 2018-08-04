using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ProblemManager : MonoBehaviour {

    public static float n;
    float numOfCircles;
    float currentNumOfCirs;

    [SerializeField]
    Transform coinSpawn;

    [SerializeField]
    GameObject coin;

	// Use this for initialization
	void Start () {

    }
	
	// Update is called once per frame
	void FixedUpdate () {

        coinSpawn.transform.position = new Vector3(GameObject.Find("Bottom_Border").transform.position.x, coinSpawn.transform.position.y, coinSpawn.transform.position.z);
        CoinUpdate();
        UpdateBorderSize();
    }

    #region Coin
    void CoinUpdate()
    {
        numOfCircles = 2 * n + 1;
        currentNumOfCirs = GameObject.FindGameObjectsWithTag("Coin").Length;

        UIUpdate();
        ControlCoinCount();
    }
    void UIUpdate()
    {
        n = (Mathf.Round(GameObject.Find("Slider").GetComponent<Slider>().value));
        GameObject.Find("Display").GetComponent<Text>().text = "n = " + n;
    }
    void applyRandomForce(GameObject coin)
    {
        float directionX = Random.Range(-1f, 1f);
        float directionY = Random.Range(-1f, 1f);

        coin.GetComponent<Rigidbody2D>().AddForce(new Vector2(directionX, directionY));
    }
    void ControlCoinCount()
    {
        if (Input.GetButtonDown("Fire1"))
        {
            GameObject coinInst = Instantiate(coin);
            coinInst.transform.position = coinSpawn.position;
            applyRandomForce(coinInst);
        }

        if (Input.GetButtonDown("Fire2"))
        {
            Destroy(GameObject.FindGameObjectWithTag("Coin"));
        }
    }
    #endregion

    #region Border
    void CreateBorder()
    {
        //if (GameObject.Find("Top_Border"))
        //{
        //    Destroy(GameObject.Find("Top_Border"));
        //}

        //GameObject top = Instantiate(GameObject.Find("Bottom_Border"));
        //top.name = "Top_Border";

        //top.transform.position = new Vector3(GameObject.Find("Bottom_Border").transform.position.x,
                                            // -GameObject.Find("Bottom_Border").transform.position.y, 
                                            // GameObject.Find("Bottom_Border").transform.position.z);

        if (GameObject.Find("Right_Border"))
        {
            Destroy(GameObject.Find("Right_Border"));
        }

        GameObject end = Instantiate(GameObject.Find("Left_Border"));
        end.name = "Right_Border";

        end.transform.position = new Vector3(GameObject.Find("Bottom_Border").transform.localScale.x * 5.111111111111112f,
                                             GameObject.Find("Right_Border").transform.position.y,
                                             GameObject.Find("Right_Border").transform.position.z);
    }

    void UpdateBorderSize()
    {
        GameObject border = GameObject.Find("Bottom_Border");
        border.transform.localScale = new Vector3(n, border.transform.localScale.y,border.transform.localScale.z);
        border.transform.position = new Vector3(2.555555555555555555555555555555556f* n, border.transform.position.y, border.transform.position.z);
        CreateBorder();
    }

#endregion
}
