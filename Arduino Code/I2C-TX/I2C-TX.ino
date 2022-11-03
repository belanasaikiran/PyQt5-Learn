
#define all_tx_Write 0x0D;  //  Register addresses  

//#include "Keyboard.h" // for key events/

#include <Wire.h>
int in1 = A0;  // RSSI1
int in2 = A1;  // RSSI2
int out1 = A2; // Imon1
int out2 = A3; // Imon2
int Tx = 0x77; // Tx Address
// int Rx = ""/; // Rx Address
byte MSB;
// byte LSB;



char *RegisterAddress[] = {
  "0x04", "0x10", "0x41", "0x42", "0x43", "0x44", "0x45", "0x46", "0x47", "0x48", "0x49", "0x4A", "0X4B"
};


char *DataValues[] = {
  "0x10", "0x10", "0x08", "0x08", "0x08", "0x08", "0x08", "0x08", "0x08", "0x08", "0x08", "0x08", "0x08"
};



String readString;
int numberOfRegisters = 13;
const char cancel = 'c';



///Initial Write to Device
void WriteToDevice() {
  for (int i = 0 ; i < numberOfRegisters ; i++) {

    Wire.beginTransmission(Tx);
    Wire.write(RegisterAddress[i]);
    Wire.write(DataValues[i]);
    Wire.endTransmission();
    Serial.print("Programmed Register ");
    Serial.print(RegisterAddress[i]);
    Serial.print(" with Data Value ");
    Serial.println(DataValues[i]);
    delay(200);

  }
}





void ModifyRegisterValue() {


  Serial.println(" Please Enter the Register Address and Data Values");
  Serial.print("Register Address: ");
  String RegAddr = Serial.readString();
  RegAddr.trim(); // remove any \r \n whitespace at the end of the String
  String dataInReg = Serial.readString();




  Serial.print(" Register Address: ");
  Serial.println(RegAddr);
  Serial.print(" Data Value: ");
  Serial.print(dataInReg);

  //  Result();

}





void setup()
{
  Wire.begin();
  pinMode(in1, INPUT);
  pinMode(in2, INPUT);
  pinMode(out1, INPUT);
  pinMode(out2, INPUT);
  Serial.begin(9600);
  while (!Serial); // wait for serial monitor
  Serial.println("\nI2C Scanner");
  WriteToDevice(); //importing the function
  Result();

}

void Result() {
  Serial.print(" | RSSI1 = ");
  Serial.print (analogRead (in1));
  Serial.print(" | RSSI2 = ");
  Serial.print (analogRead(in2));
  Serial.print(" IMONI = ");
  Serial.print (analogRead (out1));
  Serial.print(" | IMON2 = ");
  Serial.println(analogRead(out2));
  delay (2000);
}

void loop()
{

  Serial.println("Press 'c' to interrupt");
  // check for control c on key press
  while (Serial.available() == 0) {
  };

  char c = Serial.read();
  readString += c;
  //Serial.println(readString);

  if (c == cancel) {
    Serial.print("--Interrupt occured with: ", cancel);
    Serial.println(cancel);
    Serial.println(" Please Enter the Register Address & Data Values");
    Serial.print("Register Address: ");

    String RegAddr = Serial.readString();
    Serial.print(" Modified Register: ");
    Serial.println(RegAddr);
    RegAddr.trim(); // remove any \r \n whitespace at the end of the String
  }



    return ;
}
