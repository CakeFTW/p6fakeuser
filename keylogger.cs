using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

public class keyStamp
{
    public float _timeStamp;
    public char _key;
    public bool _action;
    public keyStamp(float timeStamp, char key, bool action){
        _timeStamp = timeStamp;
        _key = key;
        _action = action;
    }
}
public class keylogger : MonoBehaviour
{

float startTime;
    // keycode dictionary 
Dictionary<KeyCode, char> keycodeToChar = new Dictionary<KeyCode,char>()
{
//-------------------------LOGICAL mappings-------------------------

//Lower Case Letters
{KeyCode.A,'a'}, 
{KeyCode.B,'b'}, 
{KeyCode.C,'c'}, 
{KeyCode.D,'d'}, 
{KeyCode.E,'e'}, 
{KeyCode.F,'f'}, 
{KeyCode.G,'g'}, 
{KeyCode.H,'h'}, 
{KeyCode.I,'i'}, 
{KeyCode.J,'j'}, 
{KeyCode.K,'k'}, 
{KeyCode.L,'l'}, 
{KeyCode.M,'m'}, 
{KeyCode.N,'n'}, 
{KeyCode.O,'o'}, 
{KeyCode.P,'p'}, 
{KeyCode.Q,'q'}, 
{KeyCode.R,'r'}, 
{KeyCode.S,'s'}, 
{KeyCode.T,'t'}, 
{KeyCode.U,'u'}, 
{KeyCode.V,'v'}, 
{KeyCode.W,'w'}, 
{KeyCode.X,'x'}, 
{KeyCode.Y,'y'}, 
{KeyCode.Z,'z'} 

};

    string filePath = "C:\\Users\\Rasmus\\Documents\\p6code";
    List<keyStamp> keys = new List<keyStamp>();
    // Start is called before the first frame update
    void Start()
    {
        startTime = Time.time;
    }

    // Update is called once per frame
    void Update()
    {
        char temp = '_';
        foreach(KeyCode vKey in System.Enum.GetValues(typeof(KeyCode))){
            if(Input.GetKeyDown(vKey)){
                if(keycodeToChar.TryGetValue(vKey, out temp)){
                    keys.Add(new keyStamp(Time.time - startTime, temp, true));
                }
            }
            if(Input.GetKeyUp(vKey)){
                if(keycodeToChar.TryGetValue(vKey, out temp)){
                    keys.Add(new keyStamp(Time.time - startTime, temp, false));
                }
            }
            if(Input.GetKeyDown(vKey) && vKey == KeyCode.Escape){
                Debug.Log("saved keyinput to file at path =" + filePath);
                StreamWriter writer = new StreamWriter(filePath + "\\unitydata.txt", true);
                writer.WriteLine("UNITY");
                string a = "";
                string t = "";
                string k = "";
                
                foreach (keyStamp n in keys)
                {
                    k += n._key + ",";
                    t += n._timeStamp.ToString() + ",";
                    a += n._action.ToString() + ",";
                }
                writer.WriteLine(k);
                writer.WriteLine(t);
                writer.WriteLine(a);
                writer.Close();
            };
        }
    }
}
