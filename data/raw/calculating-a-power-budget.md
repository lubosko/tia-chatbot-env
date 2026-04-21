# Calculating a power budget


---

## Providing power for the S7-1200 CPU

All S7-1200 CPUs have an internal power supply that provides power to the CPU, any expansion modules, and the 24 V DC Sensor power output.

There are five types of expansion modules: signal modules, communication modules, signal boards, communication boards, and battery boards.

Signal modules (SM) are installed on the right-side of the CPU. You can connect the maximum number of signal modules to your CPU.

The following table shows the maximum number of signal modules you can connect to each CPU model:

| **CPU model** | **Maximum number of signal modules allowed** |
| --- | --- |
| 1211C | 0 |
| 1212C | 2 |
| 1214C | 8 |
| 1215C | 8 |
| 1217C | 8 |

Communication modules (CM) are installed on the left-side of the CPU. You can connect a maximum of 3 communication modules to any CPU.

Signal boards (SB), communications boards (CB), and battery boards (BB) are installed on top of the CPU. You can connect a maximum of 1 signal board, communication board, or battery board to any CPU.

Warning:

**Risks with exceeding the power budget**

Exceeding either power budget can cause unpredictable behavior.

Use the following information as a guide for determining how much power (or current) the CPU can provide for your configuration.

Unpredictable operation can result in death, severe personal injury, and/or property damage.

Each CPU supplies both 5 V DC and 24 V DC power:

- The CPU provides 5 V DC power for the expansion modules when an expansion module is connected. If you exceed the 5 V DC power budget, connecting the maximum number of expansion modules to your CPU might not be possible. You must remove the expansion modules until the requirement is within the power budget.
- Each CPU has a 24 V DC sensor supply that can supply 24 V DC for local input points, for relay coils on the expansion modules, or for other requirements. If your 24 V DC power requirements exceed the budget of the sensor supply, you can add an external 24 V DC power supply to your system. You must manually connect the external 24 V DC supply to the input points or relay coils on the expansion modules.

  Warning:

  **Risks with parallel connections**

  Connecting an external 24 V DC power supply in parallel with the DC sensor supply can result in a conflict between the two supplies as each seeks to establish its own preferred output voltage level. The result of this conflict can be shortened lifetime or immediate failure of one or both power supplies, with consequent unpredictable operation of the PLC system.

  The DC sensor supply on the CPU and any external power supply should provide power to different points.

  Unpredictable operation can result in death, severe personal injury, and/or property damage.

Some of the 24 V DC power input ports in the PLC system are interconnected, with a logic common circuit connecting multiple M terminals. The CPU 24 V DC power supply input, the SM relay coil power input, and a non-isolated analog power supply input are examples of circuits that are interconnected when designated as not isolated in the data sheets. All non-isolated M terminals must connect to the same external reference potential.

Warning:

**Risks with connecting non-isolated M terminals to different reference potentials**

Connecting non-isolated M terminals to different reference potentials causes unpredictable current flows. Unpredictable current flows can cause PLC damage or abnormal PLC and equipment operation.

Always be sure that all non-isolated M terminals in a PLC system are connected to the same reference potential.

PLC damage or abnormal PLC and equipment operation can cause death, severe personal injury, and/or property damage.

Information about the power budgets of the CPUs and the power requirements of the signal modules is provided in the [technical specifications](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/oS_78VQIMu51ryi8mQBz7A?section=Xc3c790cc27664f69545cb6c1feff112e).

---

## Calculating a sample power requirement

## Example power budget

The following example shows a sample calculation of the power requirements for a configuration that includes one CPU 1214C AC/DC/Relay, one SB 1223 2 x 24 V DC Input/ 2 x 24 V DC Output, one CM 1241, three SM 1223 8 DC In/8 Relay Out, and one SM 1221 8 DC In. This example has a total of 48 inputs and 36 outputs.

Note:

The CPU has already allocated the power required to drive the internal relay coils. You do not need to include the internal relay coil power requirements in a power budget calculation.

The CPU in this example provides sufficient 5 V DC current for the SMs, but does not provide enough 24 V DC current from the sensor supply for all of the inputs and expansion relay coils. The I/O requires 456 mA and the CPU provides only 400 mA. This installation requires an additional source of at least 56 mA at 24 V DC power to operate all the included 24 V DC inputs and outputs.

Table 1. Sample power budget

| **CPU power budget** | **5 V DC** | **24 V DC** |
| --- | --- | --- |
| CPU 1214C AC/DC/Relay | 1600 mA | 400 mA |
| *Minus* | | |
| **System requirements** | **5 V DC** | **24 V DC** |
| CPU 1214C, 14 inputs | - | 14 \* 4 mA = 56 mA |
| 1 SB 1223 2 x 24 V DC Input/ 2 x 24 V DC Output | 50 mA | 2 \* 4 mA = 8 mA |
| 1 CM 1241 RS422/485, 5 V power | 220 mA |  |
| 3 SM 1223, 5 V power | 3 \* 145 mA = 435 mA | - |
| 1 SM 1221, 5 V power | 1 \* 105 mA = 105 mA | - |
| 3 SM 1223, 8 inputs each | - | 3 \* 8 \* 4 mA = 96 mA |
| 3 SM 1223, 8 relay coils each | - | 3 \* 8 \* 11 mA = 264 mA |
| 1 SM 1221, 8 inputs each | - | 8 \* 4 mA = 32 mA |
| **Total requirements** | 810 mA | 456 mA |
| *Equals* | | |
| **Current balance** | **5 V DC** | **24 V DC** |
| Current balance total | 790 mA | (56 mA) |

---

## Calculating your power requirement

## Form for calculating your power budget

Use the following table to determine how much power (or current) the S7-1200 CPU can provide for your configuration. Refer to the [technical specifications](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/oS_78VQIMu51ryi8mQBz7A?section=Xc3c790cc27664f69545cb6c1feff112e) for the power budgets of your CPU model and the power requirements of your signal modules.

Table 1. Calculations for a power budget

| **CPU power budget** | **5 V DC** | **24 V DC** |
| --- | --- | --- |
|  |  |  |
| *Minus* | | |
| **System requirements** | **5 V DC** | **24 V DC** |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
| **Total requirements** |  |  |
| *Equals* | | |
| **Current balance** | **5 V DC** | **24 V DC** |
| Current balance total |  |  |