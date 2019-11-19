using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class movement : MonoBehaviour
{
    public int mass;
    public Vector3 Velocity;
    public Vector3 Force;
    public Vector3 Acceleration;

    public int stretch;
    // Update is called once per frame

    private void Start()
    {
        Velocity = new Vector3(5, 0, 0); //uncomment for Orbit movement
        //Velocity = new Vector3(0, 0, 0); // uncomment for Spring movement
        mass = 10;
    }
    void FixedUpdate()
    {
        Orbit(); //uncomment for Orbit movement
        //Spring(); //uncomment for Spring movement
        Acceleration = Force / mass;
        Velocity += Acceleration * Time.deltaTime;
        transform.position += Velocity * Time.deltaTime; 
        
    }

    void Spring()
    {
        Force = -stretch * transform.position - 3 * Velocity; 
    }

    void Orbit()
    {
        Force = -stretch * transform.position; 
    }

    void Update()
    {

    }
}
