Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> using System.Collections;
... using System.Collections.Generic;
... using UnityEngine;
... using UnityEngine.UI;
... 
... public class PlungerScript : MonoBehaviour {
... 	float power;
... 	float minPower = 0f;
... 	public float maxPower==100f;
... 	public Slider powerSlider;
... 	List<Rigidbody> ballList;
... 	bool ballReady;
... 	
...     void Start()
...     {
...       powerSlider.minValue = 0f;
... 	  powerSlider.maxValue = maxPower;
... 	  ballList = new List<RigidBody>();
... 	  
...     }
... 
... 
...     void Update()
...     {
... 		if (ballReady)
... 		{
... 			powerSlider.gameObject.SetActive(true);
... 		}
... 		else
... 		{
... 			powerSlider.gameObject.SetActive(false);
... 		}
...         powerSlider.value = power;
... 		if(ballList.Count > 0)
... 		{
... 			ballReady = true;
... 			if(Input.GetKeyDown(KeyCode.Space))
			{
				if(power <= maxPower)
				{
					power += 50 * Time.deltaTime;
				}
			}
			if(Input.GetKeyUp(KeyCode.Space))
			{
				foreach (Rigidbody r in ballList)
				{
					r.AddForce(power * Vector3.forward);
				}
			}
		}
		else 
		{
			ballReady = false;
			power = 0f;
		}
		
    }
	private void OnTriggerEnter(Collider other)
	{
		if(other.gameObject.CompareTag("Ball"))
		{
			ballList.Add(other.gameObject.GetComponent<Rigidbody>());
		}
	}
	private void OnTriggerExit(Collider other)
	{
		if(other.gameObject.CompareTag("Ball"))
		{
			ballList.Remove(other.gameObject.GetComponent<Rigidbody>());
			power = 0f;
		}
	}
}
[DEBUG ON]
[DEBUG OFF]
