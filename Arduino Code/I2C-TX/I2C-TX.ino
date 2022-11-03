
#define all_tx_Write 0x0D;  //  Register addresses  


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
  "0x04", "0x10", "0x41", "0x42", "0x43", "0x44", "0x45", "0x46", "0x47", "0x48", "0x49", "0x4A", "0x4B"
};


char *DataValues[] = {
  "0x10", "0x10", "0x08", "0x08", "0x08", "0x08", "0x08", "0x08", "0x08", "0x08", "0x08", "0x08", "0x08"
};




int numberOfRegisters = 13;
const char cancel = 'c';





String regaddr;
String dataInReg;




const char * regChar = regaddr.c_str();


const char * dataInRegChar = dataInReg.c_str();


///Initial Write to Device
void WriteToDevice() {
  for (int i = 0 ; i < numberOfRegisters ; i++) {

    Wire.beginTransmission(Tx);
    Wire.write(RegisterAddress[i], DataValues[i]);
    //    Wire.write(DataValues[i]);/
    Wire.endTransmission();
    Serial.print("Programmed Register ");
    Serial.print(RegisterAddress[i]);
    Serial.print(" with Data Value ");
    Serial.println(DataValues[i]);
    delay(200);

  }
}





void ModifyRegisterValue() {



  Wire.beginTransmission(Tx);
  Wire.write(regChar);
  Wire.write(dataInRegChar);
  Wire.endTransmission();


  Serial.print(" Updated Register : ");
  Serial.print(regaddr);
  Serial.print(" with Data Value: ");
  Serial.println(dataInReg);

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



  while (Serial.available() == 0) {
    Result();
  }     //wait for data available
  String teststr = Serial.readString();  //read until timeout
  teststr.trim();                        // remove any \r \n whitespace at the end of the String
  if (teststr == "c") {
    Serial.print("Control Interrupted with ");
    Serial.println(teststr);
    Serial.println("Please Enter Register Value: ");
    while (Serial.available() == 0) {}     //wait for data available
    regaddr = Serial.readString();  //read until timeout
    regaddr.trim();
    if (regaddr) {
      Serial.println("Register Address:");
      Serial.println(regaddr);
      delay(500);
    }
    Serial.println("Please Enter Data Value: ");
    while (Serial.available() == 0) {}     //wait for data available
    dataInReg = Serial.readString();  //read until timeout
    dataInReg.trim();
    if (dataInReg) {
      Serial.println("Data Value:");
      Serial.println(dataInReg);
    }
  }



  //  Serial.print("Updated Register ");
  //  Serial.print(regaddr);
  //  Serial.print(" with Data Value ");
  //  Serial.println(dataInReg);
  //  delay(200);

  ModifyRegisterValue();




}



