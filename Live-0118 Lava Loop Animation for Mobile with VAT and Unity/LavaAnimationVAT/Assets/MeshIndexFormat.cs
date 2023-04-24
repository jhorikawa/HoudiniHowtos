using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MeshIndexFormat : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        var mesh = GetComponent<MeshFilter>().mesh;
        mesh.indexFormat = UnityEngine.Rendering.IndexFormat.UInt32;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
