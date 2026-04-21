# Communication processor and Modbus TCP


---

## Using the serial communication interfaces

Two communication modules (CMs) and one communication board (CB) provide the interface for PtP communications:

- [CM 1241 RS232](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/8p~yNMNIsQE2TZYgy86mmQ?section=X3e9134499ddb50a0141c9501d0aa5eea)
- [CM 1241 RS422/485](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/a5o7jp6TTWYC4hAIIhN4lQ?section=Xee7344efb4be0834163d3efe31f8b70b)
- [CB 1241 RS485](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/CFGuZtvdrI9P0lc6Qj9Vgw?section=Xbc5bde19ec9f868bf0738a0227c53126)

You can connect up to three CMs (of any type) plus a CB for a total of four communication interfaces. Install the CM to the left of the CPU or another CM. Install the CB on the front of the CPU. Refer to the [installation guidelines](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/jKRGwQPMrP71Snk9RtF3zA?section=X26a0d25dfb442d436884fe33b6e54c8c) for information on module installation and removal.

The serial communication interfaces have the following characteristics:

- Have an isolated port
- Support Point-to-Point protocols
- Are configured and programmed through the point-to-point communication processor instructions
- Display transmit and receive activity by means of LEDs
- Display a diagnostic LED (CMs only)
- Are powered by the CPU: No external power connection is needed.

Refer to the technical specifications for [communication interfaces](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/nPyk~NaAI6gOiKYeW3VFmA?section=X69ed20c5f4dac6e1ab9963f9746574a8).

## LED indicators

The communication modules have three LED indicators:

- Diagnostic LED (DIAG): This LED flashes red until it is addressed by the CPU. After the CPU powers up, it checks for CMs and addresses them. The diagnostic LED begins to flash green. This means that the CPU has addressed the CM, but has not yet provided the configuration to it. The CPU downloads the configuration to the configured CMs when the program is downloaded to the CPU. After a download to the CPU, the diagnostic LED on the communication module should be a steady green.
- Transmit LED (Tx): The transmit LED illuminates when data is being transmitted out the communication port.
- Receive LED (Rx): This LED illuminates when data is being received by the communication port.

The communication board provides transmit (TxD) and receive (RxD) LEDs. It has no diagnostic LED.

---

## Biasing and terminating an RS485 network connector

Siemens provides an [RS485 network connector](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/LtO0SiK~Mx7zPUEWzq~I3A?section=X53c06df5311144a78d0397a845771293) that you can use to easily connect multiple devices to an RS485 network. The connector has two sets of terminals that allow you to attach the incoming and outgoing network cables. The connector also includes switches for selectively biasing and terminating the network.

Note:

You terminate and bias only the two ends of the RS485 network. The devices in between the two end devices are not terminated or biased. Bare cable shielding: Approximately 12 mm (1/2 in) must contact the metal guides of all locations.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/FjKbAW34PbGnzBDIFbiMpQ-VBkTPlmjVZAl17lebjV9hA/content?v=3d2dc152a41a074b)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/FjKbAW34PbGnzBDIFbiMpQ-VBkTPlmjVZAl17lebjV9hA)

|  |  |
| --- | --- |
| ① | Switch position = On: Terminated and biased |
| ② | Switch position = Off: No termination or bias |
| ③ | Switch position = On: Terminated and biased |

Table 1. Termination and bias for the RS485 connector

| **Terminating device (bias ON)** | **Non-terminating device (bias OFF)** |
| --- | --- |
|  |  |

① Pin number

② Network connector

③ Cable shield

The CB 1241 provides internal resistors for terminating and biasing the network. To terminate and bias the connection, connect TRA to TA and connect TRB to TB to include the internal resistors to the circuit. CB 1241 does not have a 9-pin connector. The following table shows the connections to a 9-pin connector on the communications partner.

Table 2. Termination and bias for the CB 1241

| **Terminating device (bias ON)** | **Non-terminating device (bias OFF)** |
| --- | --- |
|  |  |

① Connect M to the cable shield

② A = TxD/RxD - (Green wire / Pin  8)

③ B = TxD/RxD + (Red wire / Pin 3)

---

## Point-to-point (PtP) communication


---

### Overview

The CPU supports the following Point-to-Point communication (PtP) for character-based serial protocols:

- [PtP, Freeport](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/s8QhNrQ1oW~EzgWVFZYe6Q?section=X9ce622261041f91ef149ceeb8fa43f2e)
- [PtP, 3964(R)](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/EQ~dj6We~YBdDSMmw~o1aQ?section=X6fd06b6e562af43ee2833c9c5a557688)
- [USS](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/zl7JAPe2rpBpG9zbmshEZQ?section=Xcc16b6a5c9fea3f7849fd1f8c17e820f)
- [Modbus](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/DxKrWErMnDSVqYHAAKiYTA?section=X5843df0233efdedcd05edb70ef7d6ad4)

---

### PtP, Freeport communication

PtP with a Freeport, or freely constructed, protocol provides maximum freedom and flexibility, but requires extensive implementation in the user program.

|  |  |
| --- | --- |
|  | PtP enables a wide variety of possibilities:   - The ability to send information directly to an external device such as a printer - The ability to receive information from other devices such as barcode readers, RFID readers, third-party camera or vision systems, and many other types of devices - The ability to exchange information, sending and receiving data, with other devices such as GPS devices, third-party camera or vision systems, radio modems, and many more   This type of PtP communication is serial communication that uses standard UARTs to support a variety of baud rates and parity options. The RS232 and RS422/485 communication modules (CM 1241) and the RS485 communication board (CB 1241) provide the electrical interfaces for performing the PtP communications. |

## PtP Freeport over PROFIBUS or PROFINET

PtP enables you to use a PROFINET or PROFIBUS distributed I/O rack to communicate to various devices (RFID readers, GPS device, and others):

- [PROFINET](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Z44~rg1h4WN9JoB7bugZXQ?section=Xa4efc1a7d4610374ba647f805029a400): You connect the Ethernet interface of the S7-1200 CPU to a PROFINET interface module. PtP communication modules in the rack with the interface module can then provide serial communications to the PtP devices.
- [PROFIBUS](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/bUmtrcn0SdnXwmyXWr7~qA?section=X857a761a79879d39777112eb0d337413): You insert a PROFIBUS communication module in the left side of the rack with the S7-1200 CPU. You connect the PROFIBUS communication module to a rack containing a PROFIBUS interface module. PtP communication modules in the rack with the interface module can then provide serial communications to the PtP devices.

For this reason, the S7-1200 supports two sets of PtP instructions:

- [Legacy point-to-point instructions](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/JircUoXIGbtG8Ge_lw_SRg?section=X2e8a83b9ba98b255a212c1126096d60a): These instructions existed prior to version V4.0 of the S7-1200 and only work with serial communications using a CM 1241 communication module or CB 1241 communication board.
- [Point-to-point instructions](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/WokKup3hHE5TA5afrW71kw?section=X8ba04b7c52b04f768f2b30e665c08595): These instructions provide all of the functionality of the legacy instructions, plus the ability to support PtP communication modules over PROFINET and PROFIBUS distributed I/O. The point-to-point instructions allow you to access the communication modules over the distributed I/O rack.

  The S7‑1200 CM 1241 modules must have a minimum firmware version of V2.1 to use the point-to-point instructions. These modules are limited to the local rack to the left side of the S7‑1200 CPU. You can also use the point-to-point instructions with a CB 1241.

  Communications over distributed I/O use the following modules:

  | **Station** | **Module** | **Article number** | **Interface** |
  | --- | --- | --- | --- |
  | ET 200MP | CM PtP RS232 BA | 6ES7540-1AD00-0AA0 | RS232 |
  | CM PtP RS232 HF | 6ES7541-1AD00-0AB0 | RS232 |
  | CM PtP RS422/485 BA | 6ES7540-1AB00-0AA0 | RS422/RS485 |
  | CM PtP RS422/485 HF | 6ES7541-1AB00-0AB0 | RS422/RS485 |
  | ET 200SP | CM PtP | 6ES7137-6AA01-0BA0 | RS232 and RS422/RS485 |

Note:

You can use the point-to-point instructions to access a communication board, local (or left side) serial modules, serial modules over PROFINET, and serial modules over PROFIBUS. STEP 7 provides the legacy point-to-point instructions only to support existing programs. The legacy instructions still function, however, with the current S7‑1200 CPUs. You do not have to convert prior programs from one set of instructions to the other.

Note:

**CM module firmware version requirement for Time synchronization and PtP communication**

If you have enabled "CPU synchronizes the modules of the device" in the [Time synchronization](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/SOJm_tujE0cYIHaYQwbVIg?section=X86b77e8e150051231d9511e5398874b8) properties for the PROFINET interface in the device configuration, update the firmware versions of the connected communication modules to the latest available versions. Enabling module time synchronization for communication modules with old firmware versions can cause communication issues or errors.

---

### 3964(R) communication

The S7-1200 CPU supports the 3964(R) protocol to enable communication between a CM 1241, RS232 module or a CM 1241, RS422/485 module and a communication partner that uses the 3964(R) protocol. Unlike the PtP communication described above where you define specific send (transmit) and receive characteristics for the messages, the 3964(R) protocol proscribes a strict protocol using the following control characters:

- STX Start of text

  Start of character string to be transmitted
- DLE Data Link Escape

  Data transmission switchover
- ETX End of Text

  End of character string to be transmitted
- BCC Block check character
- NAK Negative Acknowledge

Refer to the chapter describing serial data transmission principles in the [S7-300 CP 341 Point-to-Point Communication, Installation, and Parameter Assignment Manual.](https://support.industry.siemens.com/cs/us/en/view/1117397) manual for a complete description of the protocol.

## Configuring the communication module

To communicate to a partner using the 3964(R) protocol, you must include one of the following communication modules in your device configuration in STEP 7:

- CM 1241, RS232
- CM 1241, RS422/485

The firmware version of the CM module must be V2.2.0 or later.

For the communication module, you then [configure the communication ports](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/z0n0zJNqfqu5cQjfXFOiUA?section=X22d93711fb0b0fbaa1e90e3d9c63f250), [priority, and protocol parameters](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/yL3VsnO85uiqkjSVATW_RQ?section=X4f749ae8c44ae510f3d61c100dd32d1b).

## Communication to a partner with the 3964(R) protocol

When you configure a CM for 3964(R) protocol, you use the standard point-to-point send and receive instructions to transfer data between the CPU and its communication partner.

The CM embeds your data from the BUFFER parameter of the send instruction into the 3964(R) protocol and sends the data to the communication partner.

The CM receives data from the communication partner by means of the 3964(R) protocol, removes the protocol information, and returns the data in the BUFFER parameter of the receive instruction.

Refer to the following point-to-point instructions:

- [Send\_P2P (Transmit send buffer data)](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/6o7LbLxLg~BIDKgSqO3ZJQ?section=X447ee9e514801ba2fa41f4b41a62ef9f)
- [Receive\_P2P (Enable receive messages)](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/M7nnz1IDZxBDpVIbxBSf3w?section=Xb30b63ed2182d7abda7aa3160a9bcb6d)

You can also use the legacy point-to-point send and receive instructions:

- [SEND\_PTP (Transmit send buffer data)](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/3zhF1GPWAOUV11cw83Dthg?section=Xc9a6126464345dd043cd773a9d0f5067)
- [RCV\_PTP (Enable receive messages)](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/OYyl3uL58luPjKF78BA8Iw?section=Xcac2c6c201a4abfd995ba47b35bd8b19)

---

### Configuring the PtP Freeport communication


---

#### Configuring the communication ports

You can use either of the following methods to configure the communication interfaces for PtP Freeport communication:

- Use the device configuration in STEP 7 to configure the port parameters (baud and parity), the send parameters and the receive parameters. The CPU stores the device configuration settings and applies the settings after a power cycle and a RUN to STOP transition.
- Use the [Port\_Config](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/3Lo~QBQ8JTeCrWwzFe7pkg?section=X8a7eb7041d7e230d0030f3bb361d6d65), [Send\_Config](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/bfoBSYRg1zg5oMTzVd_RbQ?section=X5f482bb401b94d9263fc21e62d076f30), and [Receive\_Config](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/BTLe8lvjz6Ja4F7rSuYRsw?section=Xa1b7df2bbb0c7c884b81a29a804b22a5) instructions to set the parameters. The port settings set by the instructions are valid while the CPU is in RUN mode. The port settings revert to the device configuration settings after a STOP transition or power cycle.

After [configuring the hardware devices](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/2bV0sLkfoH2lCIQuQw44fg?section=X66ef2704af54e120bb12bc5f2d041d97), you configure parameters for the communication interfaces by selecting one of the CMs in your rack or the CB, if configured.

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/OSBUC~BSCPR8vEOTDbzJvg-VBkTPlmjVZAl17lebjV9hA)

The "Properties" tab of the inspector window displays the parameters of the selected CM or CB. Select "Port configuration" to edit the following parameters:

- Protocol
- Baud rate
- Parity
- Data bits
- Stop bits
- Flow control (RS232 only)
- Wait time

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/p6vyalyP8vVfFt6c0b0E9g-VBkTPlmjVZAl17lebjV9hA/content?v=0189c35dc8db936a)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/p6vyalyP8vVfFt6c0b0E9g-VBkTPlmjVZAl17lebjV9hA)

For the CM 1241 RS232 and CB RS485 (except for [flow control](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/vO3D9h3~6H1cp2AQl8IxsA?section=X42fd8bcd964541c16277f0a79c4ebf49), which only the CM 1241 RS232 supports), the port configuration parameters are the same regardless of whether you are configuring an RS232 or an RS485 communication module or the RS485 communication board. The parameter values can differ.

For the CM 1241 RS422/485, you have additional options for port configuration as shown below. The 422 mode of the CM 1241 RS422/485 module also supports software flow control.

Select "Port configuration" to edit the following RS422/485 parameters:

- Operating mode
- Receive line initial state

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/O0RuGC7p_N9RIkIKaBksww-VBkTPlmjVZAl17lebjV9hA/content?v=75879f025bcb768d)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/O0RuGC7p_N9RIkIKaBksww-VBkTPlmjVZAl17lebjV9hA)

Your STEP 7 program can also configure the port or change the existing configuration with the [Port\_Config instruction](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/3Lo~QBQ8JTeCrWwzFe7pkg?section=X8a7eb7041d7e230d0030f3bb361d6d65). The instruction topic provides more detail about the operational mode and initial line state as well as other parameters.

| **Parameter** | **Definition** |
| --- | --- |
| Baud rate | The default value for the baud rate is 9.6 Kbits per second. Valid choices are: 300 baud, 600 baud, 1.2 Kbits, 2.4 Kbits, 4.8 Kbits, 9.6 Kbits, 19.2 Kbits, 38.4 Kbits, 57.6 Kbits, 76.8 Kbits, and 115.2 Kbits. |
| Parity | The default value for parity is no parity. Valid choices are: No parity, even, odd, mark (parity bit always set to 1), and space (parity bit always set to 0). |
| Data bits per character | The number of data bits in a character. Valid choices are 7 or 8. |
| Number of stop bits | The number of stop bits can be either one or two. The default is one. |
| Flow control | For the RS232 communication module, you can select either hardware or software [flow control](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/vO3D9h3~6H1cp2AQl8IxsA?section=X42fd8bcd964541c16277f0a79c4ebf49). If you select hardware flow control, you can select whether the RTS signal is always on, or RTS is switched. If you select software flow control, you can define the XON and XOFF characters.  The RS485 communication interfaces do not support flow control. The 422 mode of the CM 1241 RS422/485 module supports software flow control. |
| Wait time | Wait time specifies the time that the CM or CB waits to receive CTS after asserting RTS, or for receiving an XON after receiving an XOFF, depending on the type of flow control. If the wait time expires before the communication interface receives an expected CTS or XON, the CM or CB aborts the transmit operation and returns an error to the user program. You specify the wait time in milliseconds. The range is 0 to 65535 milliseconds. |
| Operating mode | This selects the operating mode RS422 or RS485 and network configurations. |
| Receive line initial state | This selects the bias options. Valid values are none, forward bias and reverse bias. Reverse bias is used to allow cable break detection. |

---

#### Managing flow control

Flow control refers to a mechanism for balancing the sending and receiving of data transmissions so that no data is lost. Flow control ensures that a transmitting device is not sending more information than a receiving device can handle. Flow control can be accomplished through either hardware or software. The RS232 CM supports both hardware and software flow control. The RS485 CM and CB do not support flow control. The 422 mode of the CM 1241 RS422/485 module supports software flow control. You specify the type of flow control either when you [configure the port](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/z0n0zJNqfqu5cQjfXFOiUA?section=X22d93711fb0b0fbaa1e90e3d9c63f250) or with the [PORT\_CFG instruction](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/gllR6joNR2ze0D8aovko1g?section=X27e9295064bde709cd5860ffebd4402d).

Hardware flow control works through the Request-to-send (RTS) and Clear-to-send (CTS) communication signals. With the RS232 CM, the RTS signal is output from pin 7 and the CTS signal is received through pin 8. The RS232 CM is a DTE (Data Terminal Equipment) device which asserts RTS as an output and monitors CTS as an input.

## Hardware flow control: RTS switched

If you enable RTS switched hardware flow control for an RS232 CM, the module sets the RTS signal active to send data. It monitors the CTS signal to determine whether the receiving device can accept data. When the CTS signal is active, the module can transmit data as long as the CTS signal remains active. If the CTS signal goes inactive, then the transmission must stop.

Transmission resumes when the CTS signal becomes active. If the CTS signal does not become active within the configured wait time, the module aborts the transmission and returns an error to the user program. You specify the wait time in the [port configuration](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/z0n0zJNqfqu5cQjfXFOiUA?section=X22d93711fb0b0fbaa1e90e3d9c63f250).

The RTS switched flow control is useful for devices that require a signal that the transmit is active. An example would be a radio modem that uses RTS as a "Key" signal to energize the radio transmitter. The RTS switched flow control will not function with standard telephone modems. Use the RTS always on selection for telephone modems.

## Hardware flow control: RTS always on

In RTS always on mode, the CM 1241 sets RTS active by default. A device such as a telephone modem monitors the RTS signal from the CM and utilizes this signal as a clear-to-send. The modem only transmits to the CM when RTS is active, that is, when the telephone modem sees an active CTS. If RTS is inactive, the telephone module does not transmit to the CM.

To allow the modem to send data to the CM at any time, configure "RTS always on" hardware flow control. The CM thus sets the RTS signal active all the time. The CM will not set RTS inactive even if the module cannot accept characters. The transmitting device must ensure that it does not overrun the receive buffer of the CM.

## Data Terminal Ready (DTR) and Data Set Ready (DSR) signal utilization

The CM sets DTR active for either type of hardware flow control. The module transmits only when the DSR signal becomes active. The state of DSR is only evaluated at the start of the send operation. If DSR becomes inactive after transmission has started, the transmission will not be paused.

## Software flow control

Software flow control uses special characters in the messages to provide flow control. You configure Hex characters that represent XON and XOFF.

XOFF indicates that a transmission must stop. XON indicates that a transmission can resume. XOFF and XON must not be the same character.

When the transmitting device receives an XOFF character from the receiving device, it stops transmitting. Transmitting resumes when the transmitting device receives an XON character. If it does not receive an XON character within the wait time that is specified in the [port configuration](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/z0n0zJNqfqu5cQjfXFOiUA?section=X22d93711fb0b0fbaa1e90e3d9c63f250), the CM aborts the transmission and returns an error to the user program.

Software flow control requires full-duplex communication, as the receiving partner must be able to send XOFF to the transmitting partner while a transmission is in progress. Software flow control is only possible with messages that contain only ASCII characters. Binary protocols cannot utilize software flow control.

---

#### Configuring transmit (send) and receive parameters

Before the CPU can engage in PtP Freeport communications, you must configure parameters for transmitting (or sending) messages and receiving messages. These parameters dictate how communications operate when messages are being transmitted to or received from a target device.

---

#### Configuring transmit (send) parameters

From the device configuration of the CPU, you configure how a communication interface transmits data by setting the "Transmit message configuration" properties for the selected interface.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/dBWleaznFDQUMZp8HXZ1Bw-VBkTPlmjVZAl17lebjV9hA/content?v=32027e13e177328e)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/dBWleaznFDQUMZp8HXZ1Bw-VBkTPlmjVZAl17lebjV9hA)

You can also dynamically configure or change the transmit message parameters from the user program by using the [Send\_Config](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/bfoBSYRg1zg5oMTzVd_RbQ?section=X5f482bb401b94d9263fc21e62d076f30) instruction.

Note:

Parameter values set from the Send\_Config instruction in the user program override the "Transmit message configuration" properties. Note that the CPU does not retain parameters set from the Send\_Config instruction in the event of power down.

| **Parameter** | **Definition** |
| --- | --- |
| RTS On delay | Specifies the amount of time to wait after activating RTS before transmission is initiated. The range is 0 to 65535 ms, with a default value of 0. This parameter is valid only when the [port configuration](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/z0n0zJNqfqu5cQjfXFOiUA?section=X22d93711fb0b0fbaa1e90e3d9c63f250) specifies hardware flow control. CTS is evaluated after the RTS On delay time has expired.  This parameter is applicable for RS232 modules only. |
| RTS Off delay | Specifies the amount of time to wait before de-activating RTS after completion of transmission. The range is 0 to 65535 ms, with a default value of 0. This parameter is valid only when the [port configuration](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/z0n0zJNqfqu5cQjfXFOiUA?section=X22d93711fb0b0fbaa1e90e3d9c63f250) specifies hardware flow control.  This parameter is applicable for RS232 modules only. |
| Send break at message start  Number of bit times in a break | Specifies that upon the start of each message, a break will be sent after the RTS On delay (if configured) has expired and CTS is active.  You specify how many bit times constitute a break where the line is held in a spacing condition. The default is 12 and the maximum is 65535, up to a limit of eight seconds. |
| Send idle line after a break  Idle line after a break | Specifies that an idle line will be sent before message start. It is sent after the break, if a break is configured. The "Idle line after a break" parameter specifies how many bit times constitute an idle line where the line is held in a marking condition. The default is 12 and the maximum is 65535, up to a limit of eight seconds. |

---

#### Configuring receive parameters

You can configure how a communication interface:

- Receives data
- Recognizes the start of a message
- Recognizes the end of a message

Set these parameters in the "Configuration of received message" properties for the selected interface.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/upapuQBbd43xS91WfLV45Q-VBkTPlmjVZAl17lebjV9hA/content?v=6813314649131fd8)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/upapuQBbd43xS91WfLV45Q-VBkTPlmjVZAl17lebjV9hA)

You can also dynamically configure or change the receive message parameters from the user program by using the [Receive\_Config instruction](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/BTLe8lvjz6Ja4F7rSuYRsw?section=Xa1b7df2bbb0c7c884b81a29a804b22a5).

Note:

Parameter values set from the Receive\_Config instruction in the user program override the "Receive message configuration" properties. Note that the CPU does not retain parameters set from the RCV\_CFG instruction in the event of power down or transition to STOP.

## Message start conditions

You can determine how the communication interface recognizes the start of a message. The start characters and the characters comprising the message go into the receive buffer until a configured end condition is met.

You can specify multiple start conditions. If you specify more than one start condition, all of the start conditions must be met before the message is considered started. For example, if you configure an idle line time and a specific start character, the CM or CB will first look for the idle line time requirement to be met and then the CM will look for the specified start character. If some other character is received (not the specified start character), the CM or CB will restart the start of message search by again looking for an idle line time.

| **Parameter** | **Definition** |
| --- | --- |
| Start on Any Character | The Any Character condition specifies that any successfully received character indicates the start of a message. This character is the first character within a message. |
| Line Break | The Line Break condition specifies that a message receive operation starts after a break character is received. |
| Idle Line | The Idle Line condition specifies that a message reception starts once the receive line has been idle or quiet for the number of specified bit times. Once this condition occurs, the start of a message begins.    ① Characters  ② Restarts the idle line timer  ③ Idle line is detected and message receive is started |
| Special condition:  Recognize message start with single character | Specifies that a particular character indicates the start of a message. This character is then the first character within a message. Any character that is received before this specific character is discarded. The default character is STX. |
| Special condition:  Recognize message start with a character sequence | Specifies that a particular character sequence from up to four configured sequences indicates the start of a message. For each sequence, you can specify up to five characters. For each character position, you specify either a specific hex character, or that the character is ignored in sequence matching (wild-card character). The last specific character of a character sequence terminates that start condition sequence.  Incoming sequences are evaluated against the configured start conditions until a start condition has been satisfied. Once the start sequence has been satisfied, evaluation of end conditions begins.  You can configure up to four specific character sequences. You use a multiple-sequence start condition when different sequences of characters can indicate the start of a message. If any one of the character sequences is matched, the message is started. |

The order of checking start conditions is:

- Idle line
- Line break
- Characters or character sequences

While checking for multiple start conditions, if one of the conditions is not met, the CM or CB will restart the checking with the first required condition. After the CM or CB establishes that the start conditions have been met, it begins evaluating end conditions.

## Example configuration: Start message on one of two character sequences

Consider the following start message condition configuration:

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/K2N2CMhjP4A~44BEzTOkBA-VBkTPlmjVZAl17lebjV9hA)

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/m3JDGUCTCm0~IPNKFy1d2A-VBkTPlmjVZAl17lebjV9hA/content?v=9a4e6d780e77ceb6)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/m3JDGUCTCm0~IPNKFy1d2A-VBkTPlmjVZAl17lebjV9hA)

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/HRI3KUdyOMnZkjOn2BO23w-VBkTPlmjVZAl17lebjV9hA/content?v=a7813dd7dd0b5f66)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/HRI3KUdyOMnZkjOn2BO23w-VBkTPlmjVZAl17lebjV9hA)

With this configuration, the start condition is satisfied when either pattern occurs:

- When a five-character sequence is received where the first character is 0x6A and the fifth character is 0x1C. The characters at positions 2, 3, and 4 can be any character with this configuration. After the fifth character is received, evaluation of end conditions begins.
- When two consecutive 0x6A characters are received, preceded by any character. In this case, evaluation of end conditions begins after the second 0x6A is received (3 characters). The character preceding the first 0x6A is included in the start condition.

Example sequences that would satisfy this start condition are:

- <any character> 6A 6A
- 6A 12 14 18 1C
- 6A 44 A5 D2 1C

## Message end conditions

You also configure how the communication interface recognizes the end of a message. You can configure multiple message end conditions. If any one of the configured conditions occurs, the message ends.

For example, you could specify an end condition with an end of message timeout of 300 milliseconds, an inter-character timeout of 40 bit times, and a maximum length of 50 bytes. The message will end if the message takes longer than 300 milliseconds to receive, or if the gap between any two characters exceeds 40 bit times, or if 50 bytes are received.

| **Parameter** | **Definition** |
| --- | --- |
| Recognize message end by message timeout | The message end occurs when the configured amount of time to wait for the message end has expired. The message timeout period begins when a start condition has been satisfied. The default is 200 ms and the range is 0 to 65535 ms.    ① Received characters  ②Start Message condition satisfied: message timer starts  ③ Message timer expires and terminates the message |
| Recognize message end by response timeout | The message end occurs when the configured amount of time to wait for a response expires before a valid start sequence is received. The response timeout period begins when a transmission ends and the CM or CB begins the receive operation. The default response timeout is 200 ms and the range is 0 to 65535 ms. If a character is not received within the response time period, RCVTIME, then an error is returned to the corresponding RCV\_PTP instruction. The response timeout does not define a specific end condition. It only specifies that a character must be successfully received within the specified time. You must configure another end condition to indicate the actual end of a message.    ① Transmitted characters  ② Received characters  ③ First character must be successfully received by this time. |
| Recognize message end by inter-character gap | The message end occurs when the maximum configured timeout between any two consecutive characters of a message has expired. The default value for the inter-character gap is 12 bit times and the maximum number is 65535 bit times, up to a maximum of eight seconds.    ① Received characters  ② Restarts the intercharacter timer  ③ The intercharacter timer expires and terminates the message. |
| Recognize message end by receiving a fixed number of characters | The message end occurs when the specified number of characters has been received. The valid range for the fixed length is 1 to 4096.  Note that for the S7-1200, this end condition is only valid for V4.0 CPUs or higher. |
| Recognize message end by max length | The message end occurs when the configured maximum number of characters has been received. The valid range for maximum length is 1 to 1024.  This condition can be used to prevent a message buffer overrun error. When this end condition is combined with timeout end conditions and the timeout condition occurs, any valid received characters are provided even if the maximum length is not reached. This allows support for varying length protocols when only the maximum length is known. |
| Read message length from message | The message itself specifies the length of the message. The message end occurs when a message of the specified length has been received. The method for specifying and interpreting the message length is described below. |
| Recognize message end with a character | The message end occurs when a specified character is received. |
| Recognize message end with a character sequence | The message end occurs when a specified character sequence is received. You can specify a sequence of up to five characters. For each character position, you specify either a specific hex character, or that the character is ignored in sequence matching.  Leading characters that are ignored characters are not part of the end condition. Trailing characters that are ignored characters are part of the end condition. |

## Example configuration: End message with a character sequence

Consider the following end message condition configuration:

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/cThojPjiIAePTv55dbMNqw-VBkTPlmjVZAl17lebjV9hA/content?v=f63d20bcba7b8584)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/cThojPjiIAePTv55dbMNqw-VBkTPlmjVZAl17lebjV9hA)

In this case, the end condition is satisfied when two consecutive 0x6A characters are received, followed by any two characters. The character preceding the 0x6A 0x6A pattern is not part of the end character sequence. Two characters following the 0x6A 0x6A pattern are required to terminate the end character sequence. The values received at character positions 4 and 5 are irrelevant, but they must be received to satisfy the end condition.

Note:

If you want your character sequence to indicate the end of the message, put the sequence in the last character positions. In the example above, if you wanted 0x6A 0x6A to end the message with no trailing characters, you would configure 0x6A in character positions 4 and 5.

## Specification of message length within the message

When you select the special condition where the message length is included in the message, you must provide three parameters that define information about the message length.

The actual message structure varies according to the protocol in use. The three parameters are as follows:

- n: the character position (1-based) within the message that starts the length specifier
- Length size: The number of bytes (one, two, or four) of the length specifier
- Length m: the number of characters following the length specifier that are not included in the length count

The ending characters do not need to be contiguous. The "Length m" value can be used to specify the length of a checksum field whose size is not included in the length field.

These fields appear in Configuration of received message under device properties:

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/Y5pg4YxChRczBLvlo1WSTw-VBkTPlmjVZAl17lebjV9hA)

**Example 1:** Consider a message structured according to the following protocol:

| **STX** | **Len (n)** | **Characters 3 to 14 counted by the length** | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ADR** | **PKE** | | **INDEX** | | **PWD** | | **STW** | | **HSW** | | **BCC** |
| **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** | **12** | **13** | **14** |
| STX | 0x0C | xx | xxxx | | xxxx | | xxxx | | xxxx | | xxxx | | xx |

Configure the receive message length parameters for this message as follows:

- n = 2 (The message length starts with byte 2.)
- Length size = 1 (The message length is defined in one byte.)
- Length m = 0 (There are no additional characters following the length specifier that are not counted in the length count. Twelve characters follow the length specifier.)

In this example, the characters from 3 to 14 inclusive are the characters counted by Len (n).

**Example 2:** Consider another message structured according to the following protocol:

| **SD1** | **Len (n)** | **Len (n)** | **SD2** | **Characters 5 to 10 counted by length** | | | | | | **FCS** | **ED** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **DA** | **SA** | **FA** | **Data unit=3 bytes** | | |
| **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** | **12** |
| xx | 0x06 | 0x06 | xx | xx | xx | xx | xx | xx | xx | xx | xx |

Configure the receive message length parameters for this message as follows:

- n = 3 (The message length starts at byte 3.)
- Length size = 1 (The message length is defined in one byte.)
- Length m = 3 (There are three characters following the length specifier that are not counted in the length. In the protocol of this example, the characters SD2, FCS, and ED are not counted in the length count. The other six characters are counted in the length count; therefore the total number of characters following the length specifier is nine.)

In this example, the characters from 5 to 10 inclusive are the characters counted by Len (n).

---

### Configuring 3964(R) communication


---

#### Configuring the 3964(R) communication ports

You can use either of the following methods to configure the communication interfaces for 3964(R) communication:

- Use the device configuration in STEP 7 to configure the port parameters. The CPU stores the device configuration settings and applies the settings after a power cycle.
- Use the [Port\_Config](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/3Lo~QBQ8JTeCrWwzFe7pkg?section=X8a7eb7041d7e230d0030f3bb361d6d65) instruction to set the port parameters. The port settings set by the instructions are valid while the CPU is in RUN mode. The port settings revert to the device configuration settings after a power cycle.

After [adding the communication interfaces to the device configuration](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/8deU3TpEgp9zfaDg2lJ2bw?section=X11f9041f9efce97d6c9fc5504fca3542), you configure parameters for the communication interfaces by selecting one of the CMs in your rack.

|  |  |
| --- | --- |
|  | The "Properties" tab of the inspector window displays the parameters of the selected CM. Select "Port configuration" to edit the following parameters:   - Protocol: 3964(R) - Operating mode  (CM 1241 (RS422/485) module only) - Receive line initial state  (CM 1241 (RS422/485) module only) - Wire break  (CM 1241 (RS422/485) module only) - Baud rate - Parity - Data bits - Stop bits |

| **Parameter** | **Definition** |
| --- | --- |
| Protocol | 3964R or Freeport. Select 3964R to configure port for 3964(R) communication |
| Operating mode\* | Full duplex (RS422) four-wire operation point-to-point. (Enabled) |
| Receive line initial state\* | Enable one of the following choices:   - None - Bias with R(A)>R(B)>=0V - Bias with R(B)>R(A)>=0V |
| Wire break\* | Enable one of the following choices:   - No wire-break check - Enable wire-break check |
| Baud rate | The default value for the baud rate is 9.6 Kbits per second. Valid choices are: 300 baud, 600 baud, 1.2 Kbits, 2.4 Kbits, 4.8 Kbits, 9.6 Kbits, 19.2 Kbits, 38.4 Kbits, 57.6 Kbits, 76.8 Kbits, and 115.2 Kbits. |
| Parity | The default value for parity is no parity. Valid choices are: No parity, even, odd, mark (parity bit always set to 1), space (parity bit always set to 0), and any parity (set parity bit to 0 for transmission; ignore parity error when receiving). |
| Data bits per character | The number of data bits in a character. Valid choices are 7 or 8. |
| Number of stop bits | The number of stop bits can be either one or two. The default is one. |

\* CM 1241 (RS422/485) module only

---

#### Configuring the 3964(R) priority and protocol parameters

You can use either of the following methods to configure the communication interfaces for 3964(R) communication:

- In the device configuration of the communication interface, click "3964(R) configuration" to set the priority and configure the protocol parameters. The CPU stores the device configuration settings and applies the settings after a power cycle.
- Use the [P3964\_Config](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/5rwJpUFKRIK~BPr5Q1EF9w?section=Xdd0bd1044ff6a10c3eddf501a41b4295) instruction to set the priority and protocol configuration parameters. The values set by the instructions are valid while the CPU is in RUN mode. The values revert to the device configuration settings after a power cycle.

|  |  |
| --- | --- |
|  | The "Properties" tab of the inspector window displays the parameters of the selected CM. Select "3964(R) configuration" to edit the following parameters:   - Priority (high or low) - Protocol parameters    - With block check (3964R)   - Use default values  Connection attempts  Transmission attempts  Character delay time  Acknowledgement delay |

| **Parameter** | **Definition** |
| --- | --- |
| Priority | High or low: The CM will be either high or low and the communication partner must be the opposite. |
| With block check (3964) | If selected, 3964(R) communication employs transmission security by including a block check character (BCC). If not selected transmission security does not include a block check character. |
| Use default values | If selected, 3964(R) uses default values for the following protocol parameters:   - Connection attempts - Transmission attempts - Character delay time - Acknowledgement delay   If not selected, you can configure values for each of these parameters. |
| Connection attempts | Number of connection attempts (default value: 6 connection attempts)  1 to 255 |
| Transmission attempts | Number of transmission attempts (default value: 6 connection attempts)  1 to 255 |
| Character delay time | Character delay time setting (depending on the set data transmission rate) (default value: 220 ms) 1 ms to 65535 ms |
| Acknowledgement delay | Acknowledgment delay time setting (depending on the set data transmission rate) (default value: 2000 ms when block check is enabled; 550 ms when block check is not enabled) 1 ms to 65535 ms |

Note:

With the exception of Priority, the protocol settings must be the same for the CM module and the communication partner.

---

### Point-to-point instructions


---

#### Common parameters for Point-to-Point instructions

Table 1. Common input parameters for the PTP instructions

| **Parameter** | **Description** |
| --- | --- |
| REQ | Many of the PtP instructions use the REQ input to initiate the operation on a low to high transition. The REQ input must be high (TRUE) for one execution of an instruction, but the REQ input can remain TRUE for as long as desired. The instruction does not initiate another operation until it has been called with the REQ input FALSE so that the instruction can reset the history state of the REQ input. This is required so that the instruction can detect the low to high transition to initiate the next operation.  When you place a PtP instruction in your program, STEP 7 prompts you to identify the instance DB. Use a unique DB for each PtP instruction call. This ensures that each instruction properly handles inputs such as REQ. |
| PORT | A port address is assigned during communication device configuration. After configuration, a default port symbolic name can be selected from the parameter assistant drop-list. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "Constants" tab of the PLC tag table. |
| Bit time resolution | Several parameters are specified in a number of bit times at the configured baud rate. Specifying the parameter in bit times allows the parameter to be independent of baud rate. All parameters that are in units of bit times can be specified to a maximum number of 65535. However, the maximum amount of time that a CM or CB can measure is eight seconds. |

The DONE, NDR, ERROR, and STATUS output parameters of the PtP instructions provide execution completion status for the PtP operations.

Table 2. DONE, NDR, ERROR, and STATUS output parameters

| **Parameter** | **Data type** | **Default** | **Description** |
| --- | --- | --- | --- |
| DONE | Bool | FALSE | Set TRUE for one execution to indicate that the last request completed without errors; otherwise, FALSE. |
| NDR | Bool | FALSE | Set TRUE for one execution to indicate that the requested action has completed without error and that the new data has been received; otherwise, FALSE. |
| ERROR | Bool | FALSE | Set TRUE for one execution to indicate that the last request completed with errors, with the applicable error code in STATUS; otherwise, FALSE. |
| STATUS | Word | 0 | Result status:   - If the DONE or NDR bit is set, then STATUS is set to 0 or to an informational code. - If the ERROR bit is set, then STATUS is set to an error code. - If none of the above bits are set, then the instruction returns status results that describe the current state of the function.   STATUS retains its value for the duration of the execution of the function. |

Note:

The DONE, NDR, and ERROR parameters are set for one execution only. Your program logic must save temporary output state values in data latches, so you can detect state changes in subsequent program scans.

Table 3. Common condition codes

| **STATUS (W#16#....)** | **Description** |
| --- | --- |
| 0000 | No error |
| 7000 | Function is not busy |
| 7001 | Function is busy with the first call. |
| 7002 | Function is busy with subsequent calls (polls after the first call). |
| 8x3A | Illegal pointer in parameter x |
| 8070 | All internal instance memory in use, too many concurrent instructions in progress |
| 8080 | Port number is illegal. |
| 8081 | Timeout, module error, or other internal error |
| 8082 | Parameterization failed because parameterization is in progress in background. |
| 8083 | Buffer overflow:  The CM or CB returned a received message with a length greater than the length parameter allowed. |
| 8090 | Internal error: Wrong message length, wrong sub-module, or illegal message  Contact customer support. |
| 8091 | Internal error: Wrong version in parameterization message  Contact customer support. |
| 8092 | Internal error: Wrong record length in parameterization message  Contact customer support. |

---

#### Condition codes

Table 1. Common error classes

| **Class description** | **Error classes** | **Description** |
| --- | --- | --- |
| Port configuration | 16#81Ax | Used to define common port configuration errors |
| Transmit configuration | 16#81Bx | Used to define common transmit configuration errors |
| Receive configuration | 16#81Cx  16#82Cx | Used to define common receive configuration errors |
| Transmission runtime | 16#81Dx | Used to define common transmission runtime errors |
| Reception runtime | 16#81Ex | Used to define common reception runtime errors |
| Signal handling | 16#81Fx | Used to define common errors associated with all signal handling |
| Pointer errors | 16#8p01 to 16#8p51 | Used for ANY pointer errors where "p" is the parameter number of the instruction |
| Embedded protocol errors | 16#848x  16#858x | Used for embedded protocol errors |

---

#### Port_Config (Configure communication parameters dynamically)

Table 1. Port\_Config (Port Configuration) instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"Port\_Config\_DB"(    REQ:=\_bool\_in\_,    PORT:=\_word\_in\_,    PROTOCOL:=\_uint\_in\_,    BAUD:=\_uint\_in\_,    PARITY:=\_uint\_in\_,    DATABITS:=\_uint\_in\_,    STOPBITS:=\_uint\_in\_,    FLOWCTRL:=\_uint\_in\_,    XONCHAR:=\_char\_in\_,    XOFFCHAR:=\_char\_in\_,    WAITTIME:=\_uint\_in\_,    MODE:=\_uint\_in\_,    LINE\_PRE:=\_uint\_in\_,    BRK\_DET:=\_uint\_in\_,    DONE=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_);** | Port\_Config allows you to change port parameters such as baud rate from your program.  You can set up the initial static configuration of the port in the device configuration properties, or just use the default values. You can execute the Port\_Config instruction in your program to change the configuration. |

1 STEP 7 automatically creates the DB when you insert the instruction.

The CPU does not permanently store the values you set with the Port\_Config instruction. The CPU restores the parameters configured in the device configuration when the CPU transitions from RUN to STOP mode and after a power cycle. See [Configuring the communication ports](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/z0n0zJNqfqu5cQjfXFOiUA?section=X22d93711fb0b0fbaa1e90e3d9c63f250) and [Managing flow control](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/vO3D9h3~6H1cp2AQl8IxsA?section=X42fd8bcd964541c16277f0a79c4ebf49) for more information.

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Activate the configuration change on rising edge of this input. (Default value: False) |
| PORT | IN | PORT | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. (Default value: 0) |
| PROTOCOL | IN | UInt | 0 - Freeport protocol (Default value)  1. 3964(R) protocol |
| BAUD | IN | UInt | Port baud rate (Default value: 6):  1 = 300 baud, 2 = 600 baud, 3 = 1200 baud, 4 = 2400 baud, 5 = 4800 baud, 6 = 9600 baud, 7 = 19200 baud, 8 = 38400 baud, 9 = 57600 baud, 10 = 76800 baud, 11 = 115200 baud |
| PARITY | IN | UInt | Port parity (Default value: 1):  1 = No parity, 2 = Even parity, 3 = Odd parity, 4 = Mark parity, 5 = Space parity |
| DATABITS | IN | UInt | Bits per character (Default value: 1):  1 = 8 data bits, 2 = 7 data bits |
| STOPBITS | IN | UInt | Stop bits (Default value: 1):  1 = 1 stop bit, 2 = 2 stop bits |
| FLOWCTRL\* | IN | UInt | Flow control (Default value: 1):  1 = No flow control, 2 = XON/XOFF, 3 = Hardware RTS always ON, 4 = Hardware RTS  switched |
| XONCHAR1 | IN | Char | Specifies the character that is used as the XON character. This is typically a DC1 character (16#11). This parameter is only evaluated if flow control is enabled. (Default value: 16#11) |
| XOFFCHAR1 | IN | Char | Specifies the character that is used as the XOFF character. This is typically a DC3 character (16#13). This parameter is only evaluated if flow control is enabled. (Default value: 16#13) |
| WAITTIME1 | IN | UInt | Specifies how long to wait for a XON character after receiving a XOFF character, or how long to wait for the CTS signal after enabling RTS (0 to 65535 ms). This parameter is only evaluated if flow control is enabled. (Default value: 2000) |
| MODE2 | IN | UInt | Specifies the selection of the module’s operating mode.   - 0 = Full duplex (RS232) - 1 = Full duplex (RS422) four-wire mode (point-to-point), transmitter always enabled - 2 = Full duplex (RS422) four-wire mode (multipoint master), transmitter always enabled - 3 = Full duplex (RS422) four-wire mode (multipoint slave), transmitter enabled while sending - 4 = Half duplex (RS485) two-wire mode |
| LINE\_PRE | IN | UInt | Specifies the inactive (idle) line condition. For RS422 and RS485 modules the idle line condition is established by applying a bias voltage to the R(A) and R(B) signals. The following selections are possible:   - 0 = Not biased (No Presetting) (default) - 1 = Biased with R(A) > R(B) ≥ 0V; RS422 only - 2 = Biased with R(B) > R(A) ≥ 0V; RS422 and RS485 |
| BRK\_DET | IN | UInt | Enables/disables communications cable break detection. Enabling cable break detection causes the module to indicate a fault when the communications cable is not connected to the module.  In RS422 Point-to-Point mode cable break detection is only possible when Receive Line Presetting is used with bias applied so that R(A) > R(B) ≥ 0V.   - 0 -= No Cable Break Detection (default) - 1 = Cable Break Detection enabled |
| DONE | OUT | Bool | TRUE for one execution after the last request was completed with no error |
| ERROR | OUT | Bool | TRUE for one execution after the last request was completed with an error |
| STATUS | OUT | Word | Execution condition code (Default value: 0) |

1 Not applicable when Protocol=1 (3964(R) protocol)

2 Only modes 0 and 1 are valid when Protocol=1 (3964(R) protocol) depending on whether your CM module is an RS232 module or RS422 module.

Table 3. Condition codes

| **STATUS (W#16#....)** | **Description** |
| --- | --- |
| 81A0 | Specific protocol does not exist. |
| 81A1 | Specific baud rate does not exist. |
| 81A2 | Specific parity option does not exist. |
| 81A3 | Specific number of data bits does not exist. |
| 81A4 | Specific number of stop bits does not exist. |
| 80A5 | Specific type of flow control does not exist. |
| 81A6 | Wait time is 0 and flow control enabled |
| 81A7 | XON and XOFF are illegal values (for example, the same value) |
| 81A8 | Error in the block header (for example, wrong block type or wrong block length) |
| 81A9 | Reconfiguration rejected because a configuration is in progress |
| 81AA | Invalid RS422/RS485 mode of operation |
| 81AB | Invalid presetting of the receive line for break detection |
| 81AC | Invalid RS232 break handling |
| 8280 | Negative acknowledgement while reading the module |
| 8281 | Negative acknowledgement while writing the module |
| 8282 | DP slave or module not available |

---

#### Send_Config (Configure serial transmission parameters dynamically)

Table 1. Send\_Config (Send Configuration) instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"Send\_Config\_DB"(    REQ:=\_bool\_in\_,    PORT:=\_word\_in\_,    RTSONDLY:=\_uint\_in\_,    RTSOFFDLY:=\_uint\_in\_,    BREAK:=\_uint\_in\_,    IDLELINE:=\_uint\_in\_,    USR\_END:=\_string\_in\_,    APP\_END:=\_string\_in\_,    DONE=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_);** | Send\_Config allows the dynamic configuration of serial transmission parameters for a PtP communication port. Any queued messages within a CM or CB are discarded when Send\_Config is executed. |

1 STEP 7 automatically creates the DB when you insert the instruction.

You can set up the initial static configuration of the port in the device configuration properties, or just use the default values. You can execute the Send\_Config instruction in your program to change the configuration.

The CPU does not permanently store the values you set with the Send\_Config instruction. The CPU restores the [parameters](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/mi0ZQs72yHnZb7VuReqWJQ?section=X358ac999dfa5ea1132da97fc314beb32) configured in the device configuration when the CPU transitions from RUN to STOP mode and after a power cycle.

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Activate the configuration change on the rising edge of this input. (Default value: False) |
| PORT | IN | PORT | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. (Default value: 0) |
| RTSONDLY | IN | UInt | Number of milliseconds to wait after enabling RTS before any Tx data transmission occurs. This parameter is only valid when hardware flow control is enabled. The valid range is 0 - 65535 ms. A value of 0 disables the feature. (Default value: 0) |
| RTSOFFDLY | IN | UInt | Number of milliseconds to wait after the Tx data transmission occurs before RTS is disabled: This parameter is only valid when hardware flow control is enabled. The valid range is 0 - 65535 ms. A value of 0 disables the feature. (Default value: 0) |
| BREAK | IN | UInt | This parameter specifies that a break will be sent upon the start of each message for the specified number of bit times. The maximum is 65535 bit times up to an eight second maximum. A value of 0 disables the feature. (Default value: 12) |
| IDLELINE | IN | UInt | This parameter specifies that the line will remain idle for the specified number of bit times before the start of each message. The maximum is 65535 bit times up to an eight second maximum. A value of 0 disables the feature. (Default value: 0) |
| USR\_END\* | IN | STRING[2] | Specifies the number and the characters in the end delimiter. The end delimiter is embedded in the transmit buffer (characters only) and marks the end of the transmitted message (characters are transmitted until the end delimiter is encountered). The end delimiter is appended to the end of the message.   - STRING[2,0,xx,yy] – End delimiter is not used (default) - STRING[2,1,xx,yy] – End delimiter is a single character - STRING[2,2,xx,yy] – End delimiter is two characters  Either USR\_END or APP\_END must have a length of zero. |
| APP\_END\* | IN | STRING[5] | Specifies the number and the characters to be appended to the transmitted message (only the characters are appended).  STRING[5,0,aa,bb,cc,dd,ee] – End char is not used (default)   - STRING[5,1,aa,bb,cc,dd,ee] – Transmit one end character - STRING[5,2,aa,bb,cc,dd,ee] – Transmit two end characters - STRING[5,3,aa,bb,cc,dd,ee]– Transmit three end characters - STRING[5,4,aa,bb,cc,dd,ee] – Transmit four end characters - STRING[5,5,aa,bb,cc,dd,ee] – Transmit five end characters |
| DONE | OUT | Bool | TRUE for one execution after the last request was completed with no error |
| ERROR | OUT | Bool | TRUE for one execution after the last request was completed with an error |
| STATUS | OUT | Word | Execution condition code (Default value: 0) |

\* Not supported for the CM and CB 1241s; you must use an empty string ("") for the parameter.

Table 3. Condition codes

| **STATUS (W#16#....)** | **Description** |
| --- | --- |
| 81B0 | Transmit interrupt configuration is not allowed. Contact customer support. |
| 81B1 | Break time is greater than the maximum allowed value. |
| 81B2 | Idle time is greater than the maximum allowed value. |
| 81B3 | Error in the block header, for example, wrong block type or wrong block length |
| 81B4 | Reconfiguration rejected because a configuration is in progress |
| 81B5 | The number of end delimiters specified is greater than two or the number of end characters is greater than five |
| 81B6 | Send configuration rejected when configured for firmware embedded protocols |
| 8280 | Negative acknowledgement while reading the module |
| 8281 | Negative acknowledgement while writing the module |
| 8282 | DP slave or module not available |

---

#### Receive_Config (Configure serial receive parameters dynamically)

Table 1. Receive\_Config (Receive Configuration) instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"Receive\_Config\_DB"(    REQ:=\_bool\_in\_,    PORT:=\_uint\_in\_,    Receive\_Conditions:=\_struct\_in\_,    DONE=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_);** | Receive\_Config performs dynamic configuration of serial receiver parameters for a PtP communication port. This instruction configures the conditions that signal the start and end of a received message. Any queued messages within a CM or CB are discarded when Receive\_Config is executed. |

1 STEP 7 automatically creates the DB when you insert the instruction.

You can set up the initial static configuration of the communication port in the device configuration properties, or just use the default values. You can execute the Receive\_Config instruction in your program to change the configuration.

The CPU does not permanently store the values you set with the Receive\_Config instruction. The CPU restores the parameters configured in the device configuration when the CPU transitions from RUN to STOP mode and after a power cycle. See the topic "[Configuring receive parameters](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/nQZx5GyPj9l1lFJ~TPSwGw?section=X0dfba602007d73e8c4bd054e1e16900d)" for more information.

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Activate the configuration change on the rising edge of this input. (Default value: False) |
| PORT | IN | PORT | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. (Default value: 0) |
| CONDITIONS | IN | CONDITIONS | The Conditions data structure specifies the starting and ending message conditions as described below. |
| DONE | OUT | Bool | TRUE for one scan, after the last request was completed with no error |
| ERROR | OUT | Bool | TRUE for one scan, after the last request was completed with an error |
| STATUS | OUT | Word | Execution condition code (Default value: 0) |

## Start conditions for the Receive\_P2P instruction

The Receive\_P2P instruction uses the configuration specified by the Receive\_Config instruction to determine the beginning and ending of point-to-point communication messages. The start of a message is determined by the start conditions. The start of a message can be determined by one or a combination of start conditions. If more than one start condition is specified, all the conditions must be satisfied before the message is started.

See the topic "[Configuring receive parameters](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/nQZx5GyPj9l1lFJ~TPSwGw?section=X0dfba602007d73e8c4bd054e1e16900d)" for a description of the message start conditions.

## Parameter CONDITIONS data type structure part 1 (start conditions)

Table 3. CONDITIONS structure for start conditions

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| STARTCOND | IN | UInt | Specifies the start condition (Default value: 1)   - 01H - Start Char - 02H - Any Char - 04H - Line Break - 08H - Idle Line - 10H - Sequence 1 - 20H - Sequence 2 - 40H - Sequence 3 - 80H - Sequence 4 |
| IDLETIME | IN | UInt | The number of bit times required for idle line timeout. (Default value: 40). Only used with an idle line condition. 0 to 65535 |
| STARTCHAR | IN | Byte | The start character used with the start character condition. (Default value: B#16#2) |
| STRSEQ1CTL | IN | Byte | Sequence 1 ignore/compare control for each character: (Default value: B#16#0)  These are the enabling bits for each character in start sequence   - 01H - Character 1 - 02H - Character 2 - 04H - Character 3 - 08H - Character 4 - 10H - Character 5   Disabling the bit associated with a character means any character will match, in this sequence position. |
| STRSEQ1 | IN | Char[5] | Sequence 1 start characters (5 characters). Default value: 0 |
| STRSEQ2CTL | IN | Byte | Sequence 2 ignore/compare control for each character. Default value: B#16#0) |
| STRSEQ2 | IN | Char[5] | Sequence 2 start characters (5 characters). Default value: 0 |
| STRSEQ3CTL | IN | Byte | Sequence 3 ignore/compare control for each character. Default value: B#16#0 |
| STRSEQ3 | IN | Char[5] | Sequence 3 start characters (5 characters). Default value: 0 |
| STRSEQ4CTL | IN | Byte | Sequence 4 ignore/compare control for each character. Default value: B#16#0 |
| STRSEQ4 | IN | Char[5] | Sequence 4 start characters (5 characters), Default value: 0 |

## Example

Consider the following received hexadecimal coded message: "**68** 10 aa **68** bb 10 aa 16" and the configured start sequences shown in the table below. Start sequences begin to be evaluated when the first 68H character is successfully received. Upon successfully receiving the fourth character (the second 68H), then start condition 1 is satisfied. Once the start conditions are satisfied, the evaluation of the end conditions begins.

The start sequence processing can be terminated due to various parity, framing, or inter-character timing errors. These errors result in no received message, because the start condition was not satisfied.

Table 4. Start conditions

| **Start condition** | **First Character** | **First Character +1** | **First Character +2** | **First Character +3** | **First Character +4** |
| --- | --- | --- | --- | --- | --- |
| 1 | **68**H | xx | xx | **68**H | xx |
| 2 | 10H | aaH | xx | xx | xx |
| 3 | dcH | aaH | xx | xx | xx |
| 4 | e5H | xx | xx | xx | xx |

## End conditions for the Receive\_P2P instruction

The end of a message is determined by the specification of end conditions. The end of a message is determined by the first occurrence of one or more configured end conditions. The section "Message end conditions" in the topic "[Configuring receive parameters](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/nQZx5GyPj9l1lFJ~TPSwGw?section=X0dfba602007d73e8c4bd054e1e16900d)" describes the end conditions that you can configure in the Receive\_Config instruction.

You can configure the end conditions in either the properties of the communication interface in the device configuration, or from the Receive\_Config instruction. Whenever the CPU transitions from STOP to RUN, the receive parameters (both start and end conditions) return to the device configuration settings. If the STEP 7 user program executes Receive\_Config, then the settings are changed to the Receive\_Config conditions.

## Parameter CONDITIONS data type structure part 2 (end conditions)

Table 5. CONDITIONS structure for end conditions

| **Parameter** | **Parameter type** | **Data type** | **Description** |
| --- | --- | --- | --- |
| ENDCOND | IN | UInt  0 | This parameter specifies message end condition:   - 01H - Response time - 02H - Message time - 04H - Inter-character gap - 08H - Maximum length - 10H - N + LEN + M - 20H - Sequence |
| MAXLEN | IN | UInt  1 | Maximum message length: Only used when the maximum length end condition is selected. 1 to 1024 bytes |
| N | IN | UInt  0 | Byte position within the message of the length field. Only used with the N + LEN + M end condition. 1 to 1022 bytes |
| LENGTHSIZE | IN | UInt  0 | Size of the byte field (1, 2, or 4 bytes). Only used with the N + LEN + M end condition. |
| LENGTHM | IN | UInt  0 | Specify the number of characters following the length field that are not included in the value of the length field. This is only used with the N + LEN + M end condition. 0 to 255 bytes |
| RCVTIME | IN | UInt  200 | Specify how long to wait for the first character to be received. The receive operation will be terminated with an error if a character is not successfully received within the specified time. This is only used with the response time condition. (0 to 65535 bit times with an 8 second maximum)  This parameter is not a message end condition since evaluation terminates when the first character of a response is received. It is an end condition only in the sense that it terminates a receiver operation because no response is received when a response is expected. You must select a separate end condition. |
| MSGTIME | IN | UInt  200 | Specify how long to wait for the entire message to be completely received once the first character has been received. This parameter is only used when the message timeout condition is selected. (0 to 65535 milliseconds) |
| CHARGAP | IN | UInt  12 | Specify the number of bit times between characters. If the number of bit times between characters exceeds the specified value, then the end condition will be satisfied. This is only used with the inter-character gap condition. (0 to 65535 bit times up to 8 second maximum) |
| ENDSEQ1CTL | IN | Byte  B#16#0 | Sequence 1 ignore/compare control for each character:  These are the enabling bits for each character for the end sequence. Character 1 is bit 0, character 2 is bit 1, …, character 5 is bit 4. Disabling the bit associated with a character means any character will match, in this sequence position. |
| ENDSEQ1 | IN | Char[5]  0 | Sequence 1 start characters (5 characters) |

Table 6. Condition codes

| **STATUS (W#16#....)** | **Description** |
| --- | --- |
| 81C0 | Illegal start condition selected |
| 81C1 | Illegal end condition selected, no end condition selected |
| 81C2 | Receive interrupt enabled and this is not possible. |
| 81C3 | Maximum length end condition is enabled and max length is 0 or > 1024. |
| 81C4 | Calculated length is enabled and N is >= 1023. |
| 81C5 | Calculated length is enabled and length is not 1, 2 or 4. |
| 81C6 | Calculated length is enabled and M value is > 255. |
| 81C7 | Calculated length is enabled and calculated length is > 1024. |
| 81C8 | Response timeout is enabled and response timeout is zero. |
| 81C9 | Inter-character gap timeout is enabled and it is zero. |
| 81CA | Idle line timeout is enabled and it is zero. |
| 81CB | End sequence is enabled but all chars are "don't care". |
| 81CC | Start sequence (any one of 4) is enabled but all characters are "don't care". |
| 81CD | Invalid receive message overwrite protection selection error |
| 81CE | Invalid receive message buffer handling on STOP to RUN transition selection error |
| 81CF | Error in the block header, for example, wrong block type or wrong block length |
| 8281 | Negative acknowledgement while writing the module |
| 8282 | DP slave or module not available |
| 82C0 | Reconfiguration rejected because a configuration is in progress |
| 82C1 | The specified value for the number of messages that the module can buffer is greater than the maximum permitted value. |
| 82C2 | Receive configuration rejected when configured for firmware embedded protocols |
| 8351 | Data type not allowed at this Variant pointer |

---

#### P3964_Config (Configuring the 3964(R) protocol)

Table 1. P3964\_Config (Configuring the 3964(R) protocol) instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"P3964\_Config\_DB"(    REQ:=\_bool\_in\_,    PORT:=\_uint\_in\_,    BCC:=\_usint\_in,    Priority:= \_usint\_in,    CharacterDelayTime:=\_uint\_in,    AcknDelayTime:= \_uint\_in,    BuildupAttempts:=\_usint\_in\_,    RepetitionAttempts:=\_usint\_in\_,    DONE=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_);** | P3964\_Config allows you to change priority and protocol parameters during runtime.  You can set up the initial static configuration of the port in the device configuration properties, or just use the default values. You can execute the P3964\_Config instruction in your program to change the configuration. |

1 STEP 7 automatically creates the DB when you insert the instruction.

The CPU does not permanently store the values you set with the P3964\_Config instruction. The CPU restores the parameters configured in the device configuration after a power cycle of the CPU. See [Configuring the 3964(R) communication priority and protocol parameters](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/yL3VsnO85uiqkjSVATW_RQ?section=X4f749ae8c44ae510f3d61c100dd32d1b) for more information.

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Activate the configuration change on rising edge of this input. (Default value: False) |
| PORT | IN | UInt | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. (Default value: 0) |
| BCC | IN | USInt | Activates/deactivates the use of the block check   - 0 = without block check - 1 = with block check |
| Priority | IN | UInt | Selection of the priority   - 0 = low priority - 1 = high priority   The priority of the CM must be the opposite of the priority of the communication partner. |
| CharacterDelayTime | IN | UInt | Character delay time setting (depending on the set data transmission rate) (default value: 220 ms)  1 ms to 65535 ms |
| AcknDelayTime | IN | UInt | Acknowledgment delay time setting (depending on the set data transmission rate) (default value: 2000 ms)  1 ms to 65535 ms |
| BuildupAttempts | IN | UInt | Number of connection attempts (default value: 6 connection attempts)  1 to 255 |
| RepetitionAttempts | IN | UInt | Number of transmission attempts (default value: 6 connection attempts)  1 to 255 |
| DONE | OUT | Bool | TRUE for one execution after the last request was completed with no error |
| ERROR | OUT | Bool | TRUE for one execution after the last request was completed with an error |
| STATUS | OUT | Word | Execution condition code (Default value: 0) |

Table 3. Condition codes

| **STATUS (W#16#....)** | **Description** |
| --- | --- |
| 16#8380 | Parameter assignment error: Invalid value for "Character delay time". |
| 16#8381 | Parameter assignment error: Invalid value for "Response timeout". |
| 16#8382 | Parameter assignment error: Invalid value for "Priority". |
| 16#8383 | Parameter assignment error: Invalid value for "Block check" |
| 16#8384 | Parameter assignment error: Invalid value for "Connection attempts". |
| 16#8385 | Parameter assignment error: Invalid value for "Transmission attempts". |
| 16#8386 | Runtime error: Number of connection attempts exceeded |
| 16#8387 | Runtime error: Number of transmission attempts exceeded |
| 16#8388 | Runtime error: Error at the "Block check character"  The internally calculated value of the block check character does not correspond to the block check character received by the partner at the connection end. |
| 16#8389 | Runtime error: Invalid character received while waiting for free receive buffer |
| 16#838A | Runtime error: Logical error during receiving.  After DLE was received, a further random character (other than DLE or ETX) was received. |
| 16#838B | Runtime error: Character delay time exceeded |
| 16#838C | Runtime error: Wait time for free receive buffer has started |
| 16#838D | Runtime error: frame repetition does not start within 4 s after NAK |
| 16#838E | Runtime error: In idle mode, one or several characters (other than NAK or STX) were received. |
| 16#838F | Runtime error: Initialization conflict - Both partners have set high priority |
| 16#8391 | Parameter assignment error: 3964 configuration data rejected because Freeport is set |

---

#### Send_P2P (Transmit send buffer data)

Table 1. Send\_P2P (Send Point-to-Point data) instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"Send\_P2P\_DB"(    REQ:=\_bool\_in\_,    PORT:=\_word\_in\_,    BUFFER:=\_variant\_in\_,    LENGTH:=\_uint\_in\_,    DONE=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_);** | Send\_P2P initiates the transmission of the data and transfers the assigned buffer to the communication interface. The CPU program continues while the CM or CB sends the data at the assigned baud rate. Only one send operation can be pending at a given time. The CM or CB returns an error if a second Send\_P2P is executed while the CM or CB is already transmitting a message. |

1 STEP 7 automatically creates the DB when you insert the instruction.

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Activates the requested transmission on the rising edge of this transmission enable input. This initiates transfer of the contents of the buffer to the Point-to-Point communication interface. (Default value: False) |
| PORT | IN | PORT | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. (Default value: 0) |
| BUFFER | IN | Variant | This parameter points to the starting location of the transmit buffer. (Default value: 0)  **Note:** Boolean data or Boolean arrays are not supported. |
| LENGTH | IN | UInt | Transmitted frame length in bytes (Default value: 0)  When transmitting a complex structure, always use a length of 0. When the length is 0, the instruction transmits the entire frame. |
| DONE | OUT | Bool | TRUE for one scan, after the last request was completed with no error |
| ERROR | OUT | Bool | TRUE for one scan, after the last request was completed with an error |
| STATUS | OUT | Word | Execution condition code (Default value: 0) |

While a transmit operation is in progress, the DONE and ERROR outputs are FALSE. When a transmit operation is complete, either the DONE or the ERROR output will be set TRUE to show the status of the transmit operation. While DONE or ERROR is TRUE, the STATUS output is valid.

The instruction returns a status of 16#7001 if the communication interface accepts the transmit data. Subsequent Send\_P2P executions return 16#7002, if the CM or CB is still busy transmitting. When the transmit operation is complete, the CM or CB returns the status of the transmit operation as 16#0000 (if no errors occurred). Subsequent executions of Send\_P2P with REQ low return a status of 16#7000 (not busy).

The following diagrams show the relationship of the output values to REQ. This assumes that the instruction is called periodically to check for the status of the transmission process. In the diagram below, it is assumed that the instruction is called every scan (represented by the STATUS values).

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/sCBcV0R5KXVbAyqsAKN6iA-VBkTPlmjVZAl17lebjV9hA)

The following diagram shows how the DONE and STATUS parameters are valid for only one scan if the REQ line is pulsed (for one scan) to initiate the transmit operation.

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/fGGQUUteV_qO6uPBNvTQlg-VBkTPlmjVZAl17lebjV9hA)

The following diagram shows the relationship of DONE, ERROR and STATUS parameters when there is an error.

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/NU6ddTPkTmsC4d~boaIfQA-VBkTPlmjVZAl17lebjV9hA)

The DONE, ERROR and STATUS values are only valid until Send\_P2P executes again with the same instance DB.

Table 3. Condition codes

| **STATUS (W#16#....)** | **Description** |
| --- | --- |
| 81D0 | New request while transmitter active |
| 81D1 | Transmit aborted because of no CTS within wait time |
| 81D2 | Transmit aborted because of no DSR from the DCE device |
| 81D3 | Transmit aborted because of queue overflow (transmit more than 1024 bytes) |
| 81D5 | Reverse bias signal (wire break condition) |
| 81D6 | Transmission request rejected because end delimiter was not found in the transmit buffer |
| 81D7 | Internal error / error in synchronization between FB and CM |
| 81D8 | Transmission attempt rejected because the port has not been configured |
| 81DF | CM has reset the interface to the FB due to one of the following reasons   - The module has restarted (Power cycle) - The CPU has reached a breakpoint - The module has been reparameterized   In each case the module indicates this code in the Status parameter. The module resets Status and Error to zero after the first received record for SEND\_P2P. |
| 8281 | Negative acknowledgement while writing the module |
| 8282 | DP slave or module not available |
| 8301 | Illegal syntax ID at an ANY pointer |
| 8322 | Range length error when reading a parameter |
| 8324 | Range error when reading a parameter |
| 8328 | Alignment error when reading a parameter |
| 8332 | The parameter contains a DB number that is higher than the highest permitted number (DB number error). |
| 833A | The DB for the BUFFER parameter does not exist. |

Note:

**Setting the maximum record length for Profibus communication**

When using a CM1243-5 Profibus Master module to control an ET 200SP or ET 200MP Profibus device that uses an RS232, RS422, or RS485 point-to-point module, you need to explicitly set the "max\_record\_len" data block tag to 240 as defined below:

Set "max\_record\_len" in the instance DB (for example, "Send\_P2P\_DB".max\_record\_len) to 240 after running any configuration instruction such as Port\_Config, Send\_Config, or Receive\_Config.

Explicitly assigning max\_record\_len is only necessary with Profibus communication; Profinet communication already uses a valid max\_record\_len value.

---

#### LEN and DATA parameter usage for communication instructions

## Interaction of the LENGTH and BUFFER parameters

The minimum size of data that can be transmitted by the SEND\_P2P instruction is one byte. The BUFFER parameter determines the size of the data to be transmitted. You cannot use the data type Bool or arrays of Bool for the BUFFER parameter.

You can always set the LENGTH parameter to 0 and ensure that SEND\_P2P sends the entire data structure represented by the BUFFER parameter. If you only want to send part of a data structure in the BUFFER parameter, you can set LENGTH as follows:

Table 1. LENGTH and BUFFER parameters

| **LENGTH** | **BUFFER** | **Description** |
| --- | --- | --- |
| = 0 | Not used | The complete data is sent as defined at the BUFFER parameter. You do not need to specify the number of transmitted bytes when LENGTH = 0. |
| > 0 | Elementary data type | The LENGTH value must contain the byte count of this data type. For example, for a Word value, the LENGTH must be two. For a Dword or Real, the LENGTH must be four. Otherwise, nothing is transferred and the error 8088H is returned. |
| Structure | The LENGTH value can contain a byte count less than the complete byte length of the structure, in which case the instruction sends only the first n bytes of the structure from the BUFFER, where n = LENGTH. Since the internal byte organization of a structure cannot always be determined, you might get unexpected results. In this case, use a LENGTH of 0 to send the complete structure. |
| Array | The LENGTH value must contain a byte count that is less than or equal to the complete byte length of the array and which must be a multiple of the data element byte count. For example, the LENGTH parameter for an array of Words must be a multiple of two and for an array of Reals, a multiple of four. When LENGTH is specified, the instruction transfers the number of array elements that correspond to the LENGTH value in bytes. If your BUFFER, for example, contains an array of 15 Dwords (60 total bytes), and you specify a LENGTH of 20, then the first five Dwords in the array are transferred.  The LENGTH value must be a multiple of the data element byte count. Otherwise, STATUS = 8088H, ERROR = 1, and no transmission occurs. |
| String | The LENGTH parameter contains the number of characters to be transmitted. Only the characters of the String are transmitted. The maximum and actual length bytes of the String are not transmitted. |

---

#### Receive_P2P (Enable receive messages)

Table 1. Receive\_P2P (Receive Point-to-Point) instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"Receive\_P2P\_DB"(    PORT:=\_word\_in\_,    BUFFER:=\_variant\_in\_,    NDR=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    LENGTH=>\_uint\_out\_);** | Receive\_P2P checks for messages that have been received in the CM or CB. If a message is available, it will be transferred from the CM or CB to the CPU. An error returns the appropriate STATUS value. |

1 STEP 7 automatically creates the DB when you insert the instruction.

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| PORT | IN | PORT | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. (Default value: 0) |
| BUFFER | IN | Variant | This parameter points to the starting location of the receive buffer. This buffer should be large enough to receive the maximum length message.  Boolean data or Boolean arrays are not supported. (Default value: 0) |
| NDR | OUT | Bool | TRUE for one execution when new data is ready and operation is complete with no errors. |
| ERROR | OUT | Bool | TRUE for one execution after the operation was completed with an error. |
| STATUS | OUT | Word | Execution condition code (Default value: 0) |
| LENGTH | OUT | UInt | Length of the returned message in bytes (Default value: 0) |

The STATUS value is valid when either NDR or ERROR is TRUE. The STATUS value provides the reason for termination of the receive operation in the CM or CB. This is typically a positive value, indicating that the receive operation was successful and that the receive process terminated normally. If the STATUS value is negative (the Most Significant Bit of the hexadecimal value is set), the receive operation was terminated for an error condition such as parity, framing, or overrun errors.

Each PtP communication interface can buffer up to a maximum of 1024 bytes. This could be one large message or several smaller messages. If more than one message is available in the CM or CB, the Receive\_P2P instruction returns the oldest message available. A subsequent Receive\_P2P instruction execution returns the next oldest message available.

Table 3. Condition codes

| **STATUS (W#16#...)** | **Description** |
| --- | --- |
| 0000 | No buffer present |
| 0094 | Message terminated due to received maximum character length |
| 0095 | Message terminated because of message timeout |
| 0096 | Message terminated because of inter-character timeout |
| 0097 | Message terminated because of response timeout |
| 0098 | Message terminated because the "N+LEN+M" length condition was satisfied |
| 0099 | Message terminated because of end sequence was satisfied |
| 8085 | LENGTH parameter has a value of 0 or is greater than 1KB. |
| 8088 | The LENGTH parameter or the received length is longer than the area specified in BUFFER or the received length is longer than the area specified in BUFFER. |
| 8090 | Incorrect configuration message, wrong message length, wrong submodule, illegal message |
| 81E0 | Message terminated because the receive buffer is full |
| 81E1 | Message terminated due to parity error |
| 81E2 | Message terminated due to framing error |
| 81E3 | Message terminated due to overrun error |
| 81E4 | Message terminated because calculated length exceeds buffer size |
| 81E5 | Reverse bias signal (wire break condition) |
| 81E6 | The message queue is full. This error is reported without data. If it occurs, the module toggles between an error free data transfer and this error. |
| 81E7 | Internal error, error in synchronization between instruction and CM: set when a sequence error is detected |
| 81E8 | Message terminated, inter-character timeout expired before the end of message criteria was satisfied |
| 81E9 | Modbus CRC error detected (Only used by modules that support CRC generation/checking for the Modbus protocol) |
| 81EA | Modbus telegram is too short (Only used by modules that support CRC generation/checking for the Modbus protocol) |
| 81EB | Message terminated, because maximum message size exceeded |
| 8201 | Illegal syntax ID at an ANY pointer |
| 8223 | Range length error when writing a parameter. The parameter is located either entirely or partly outside the range of an address or that the length of a bit range is not a multiple of 8 with an ANY pointer. |
| 8225 | Range error when writing a parameter. The parameter is located in a range that is illegal for the system function. |
| 8229 | Alignment error when writing a parameter. The referenced parameter is located at bit address that is not equal to 0. |
| 8230 | Parameter is located in a read-only global DB |
| 8231 | Parameter is located in a read-only instance DB. |
| 8232 | Parameter contains a DB number that is higher than the highest block number allowed (DB number error). |
| 823A | The DB for the BUFFER parameter does not exist. |
| 8280 | Negative acknowledgement while reading the module |
| 8282 | DP slave or module not available |

---

#### Receive_Reset (Delete receive buffer)

Table 1. Receive\_Reset (Receiver Reset) instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"Receive\_Reset\_DB"(    REQ:=\_bool\_in\_,    PORT:=\_word\_in\_,    DONE=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_);** | Receive\_Reset clears the receive buffers in the CM or CB. |

1 STEP 7 automatically creates the DB when you insert the instruction.

Table 2. Data types for parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Activates the receiver reset on the rising edge of this enable input (Default value: False) |
| PORT | IN | PORT | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. (Default value: 0) |
| DONE | OUT | Bool | When TRUE for one scan, indicates that the last request was completed without errors. |
| ERROR | OUT | Bool | When TRUE, shows that the last request was completed with errors. Also, when this output is TRUE, the STATUS output will contain related error codes. |
| STATUS | OUT | Word | Error code (Default value: 0) |

---

#### Signal_Get (Query RS-232 signals)

Table 1. Signal\_Get (Get RS232 signals) instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"Signal\_Get\_DB"(    REQ:=\_bool\_in\_,    PORT:=\_uint\_in\_,    NDR=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    DTR=>\_bool\_out\_,    DSR=>\_bool\_out\_,    RTS=>\_bool\_out\_,    CTS=>\_bool\_out\_,    DCD=>\_bool\_out\_,    RING=>\_bool\_out\_);** | Signal\_Get reads the current states of RS232 communication signals.  This function is valid only for the RS232 CM. |

1 STEP 7 automatically creates the DB when you insert the instruction.

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Get RS232 signal state values on the rising edge of this input (Default value: False) |
| PORT | IN | PORT | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. |
| NDR | OUT | Bool | TRUE for one scan, when new data is ready and the operation is complete with no errors |
| ERROR | OUT | Bool | TRUE for one scan, after the operation was completed with an error |
| STATUS | OUT | Word | Execution condition code (Default value: 0) |
| DTR | OUT | Bool | Data terminal ready, module ready (output). Default value: False |
| DSR | OUT | Bool | Data set ready, communication partner ready (input). Default value: False |
| RTS | OUT | Bool | Request to send, module ready to send (output). Default value: False |
| CTS | OUT | Bool | Clear to send, communication partner can receive data (input). Default value: False |
| DCD | OUT | Bool | Data carrier detect, receive signal level (always False, not supported) |
| RING | OUT | Bool | Ring indicator, indication of incoming call (always False, not supported) |

Table 3. Condition codes

| **STATUS (W#16#....)** | **Description** |
| --- | --- |
| 81F0 | CM or CB is RS485 and no signals are available |
| 81F4 | Error in the block header, for example, wrong block type or wrong block length |
| 8280 | Negative acknowledgement while reading the module |
| 8282 | DP slave or module not available |

---

#### Signal_Set (Set RS-232 signals)

Table 1. Signal\_Set (Set RS232 signals) instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"Signal\_Set\_DB"(    REQ:=\_bool\_in\_,    PORT:=\_word\_in\_,    SIGNAL:=\_byte\_in\_,    RTS:=\_bool\_in\_,    DTR:=\_bool\_in\_,    DSR:=\_bool\_in\_,    DONE=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_);** | Signal\_Set sets the states of RS232 communication signals.  This function is valid only for the RS232 CM. |

1 STEP 7 automatically creates the DB when you insert the instruction.

Table 2. Data types for parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Start the set RS232 signals operation, on the rising edge of this input (Default value: False) |
| PORT | IN | PORT | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. (Default value: 0) |
| SIGNAL | IN | Byte | Selects which signal to set: (multiple allowed). Default value: 0   - 01H = Set RTS - 02H = Set DTR - 04H = Set DSR |
| RTS | IN | Bool | Request to send, module ready to send value to set (true or false), Default value: False |
| DTR | IN | Bool | Data terminal ready, module ready to send value to set (true or false). Default value: False |
| DSR | IN | Bool | Data set ready (only applies to DCE type interfaces), not used. |
| DONE | OUT | Bool | TRUE for one execution after the last request was completed with no error |
| ERROR | OUT | Bool | TRUE for one execution after the last request was completed with an error |
| STATUS | OUT | Word | Execution condition code (Default value: 0) |

Table 3. Condition codes

| **STATUS (W#16#....)** | **Description** |
| --- | --- |
| 81F0 | CM or CB is RS485 and no signals can be set |
| 81F1 | Signals cannot be set because of Hardware flow control |
| 81F2 | Cannot set DSR because module is DTE |
| 81F3 | Cannot set DTR because module is DCE |
| 81F4 | Error in the block header, for example, wrong block type or wrong block length |
| 8280 | Negative acknowledgement while reading the module |
| 8281 | Negative acknowledgement while writing the module |
| 8282 | DP slave or module not available |

---

#### Get_Features

Table 1. Get\_Features (Get advanced features) instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"Get\_Features\_DB"(    REQ:=\_bool\_in\_,    PORT:=\_word\_in\_,    NDR:=\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    MODBUS\_CRC=>\_bool\_out\_,    DIAG\_ALARM=>\_bool\_out\_,    SUPPLY\_VOLT=>\_bool\_out);** | Get\_Features reads the advanced feature capabilities of a module. |

1 STEP 7 automatically creates the DB when you insert the instruction.

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Activate the configuration change on the rising edge of this input. (Default value: False) |
| PORT | IN | PORT | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. (Default value: 0) |
| NDR | OUT | Bool | Indicates that new data is ready. |
| ERROR | OUT | Bool | TRUE for one scan, after the last request was completed with an error |
| STATUS | OUT | Word | Execution condition code (Default value: 0) |
| MODBUS\_CRC\* | OUT | Bool | MODBUS CRC generation and checking |
| DIAG\_ALARM\* | OUT | Bool | Diagnostic alarm generation |
| SUPPLY\_VOLT\* | OUT | Bool | Diagnostics for missing supply voltage L+ is available |

\*Get\_Features returns TRUE (1) if the feature is available, FALSE (0) if the feature is not available

---

#### Set_Features

Table 1. Set\_Features (Set advanced features) instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"Set\_Features\_DB"(    REQ:=\_bool\_in\_,    PORT:=\_word\_in\_,    EN\_MODBUS\_CRC:=\_bool\_in\_,    EN\_DIAG\_ALARM:=\_bool\_in\_,    EN\_SUPPLY\_VOLT:=\_bool\_in\_,    DONE=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_);** | Set\_Features sets the advanced features that a module supports. |

1 STEP 7 automatically creates the DB when you insert the instruction.

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Activate the configuration change on the rising edge of this input. (Default value: False) |
| PORT | IN | PORT | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. (Default value: 0) |
| EN\_MODBUS\_CRC | IN | Bool | Enable MODBUS CRC generation and checking:   - 0: CRC calculation tuned OFF (default) - 1: CRC calculation turned ON   Note: Only V2.1 CMs, V4.x CPUs with CBs, and CM PtP modules for distributed I/O support this parameter. |
| EN\_DIAG\_ALARM | IN | Bool | Enable diagnostic alarm generation:   - 0: Diagnostic alarm turned OFF - 1: Diagnostic alarm turned ON (default) |
| EN\_SUPPLY\_VOLT | IN | Bool | Enable diagnostics for missing supply voltage L+:   - 0: Supply voltage diagnostic disabled (default) - 1: Supply voltage diagnostic enabled |
| DONE | OUT | Bool | Indicates that set features is done |
| ERROR | OUT | Bool | TRUE for one scan, after the last request was completed with an error |
| STATUS | OUT | Word | Execution condition code (Default value: 0) |

---

### Programming the PtP communications


---

#### Programming overview

STEP 7 provides extended instructions that enable the user program to perform Point-to-Point communications with a protocol designed and implemented in the user program. These instructions fall into two categories:

- Configuration instructions
- Communication instructions

## Configuration instructions

Before your user program can engage in PtP communication, you must configure the communication interface port and the parameters for sending data and receiving data.

You can perform the port configuration and message configuration for each CM or CB through the device configuration or through these instructions in your user program:

- [Port\_Config](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/3Lo~QBQ8JTeCrWwzFe7pkg?section=X8a7eb7041d7e230d0030f3bb361d6d65)
- [Send\_Config](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/bfoBSYRg1zg5oMTzVd_RbQ?section=X5f482bb401b94d9263fc21e62d076f30)
- [Receive\_Config](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/BTLe8lvjz6Ja4F7rSuYRsw?section=Xa1b7df2bbb0c7c884b81a29a804b22a5)

## Communication instructions

The PtP communication instructions enable the user program to send messages to and receive messages from the communication interfaces. For information about transferring data with these instructions, see the section on [data consistency](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/dDSAEcf_YTVb3G9mxvngEg?section=Xa82b0fd901da8408ecc0617160b6d748).

All of the PtP functions operate asynchronously. The user program can use a polling architecture to determine the status of transmissions and receptions. Send\_P2P and Receive\_P2P can execute concurrently. The communication modules and communication board buffer the transmit and receive messages as necessary up to a maximum buffer size of 1024 bytes.

The CMs and CB send messages to and receive messages from the actual point-to-point devices. The message protocol is in a buffer that is either received from or sent to a specific communication port. The buffer and port are parameters of the send and receive instructions:

- [Send\_P2P](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/6o7LbLxLg~BIDKgSqO3ZJQ?section=X447ee9e514801ba2fa41f4b41a62ef9f)
- [Receive\_P2P](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/M7nnz1IDZxBDpVIbxBSf3w?section=Xb30b63ed2182d7abda7aa3160a9bcb6d)

Additional instructions provide the capability to reset the receive buffer, and to get and set specific RS232 signals:

- [Receive\_Reset](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/V0IXG5gLPWD9SUcxtBjZrg?section=X7a45c671ef62b6b6761f363878e55528)
- [Signal\_Get](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/YwgWygfuBQTYkacL14BCdA?section=Xd84a158a924c36efd0ee79fb3dbb8c39)
- [Signal\_Set](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/PvvAHJOUc4qpCYlQUhI1zg?section=Xa317e2d94c252e20e6400827bf51f3fa)

---

#### Polling architecture

The STEP 7 user program must call the S7-1200 point-to-point instructions cyclically/periodically to check for received messages. Polling the send tells the user program when the transmit has completed.

## Polling architecture: master

The typical sequence for a master is as follows:

1. A [Send\_P2P](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/6o7LbLxLg~BIDKgSqO3ZJQ?section=X447ee9e514801ba2fa41f4b41a62ef9f) instruction initiates a transmission to the CM or CB.
2. The Send\_P2P instruction executes on subsequent scans to poll for the transmit complete status.
3. When the Send\_P2P instruction indicates that the transmission is complete, the user code can prepare to receive the response.
4. The [Receive\_P2P](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/M7nnz1IDZxBDpVIbxBSf3w?section=Xb30b63ed2182d7abda7aa3160a9bcb6d) instruction executes repeatedly to check for a response. When the CM or CB has collected a response message, the Receive\_P2P instruction copies the response to the CPU and indicates that new data has been received.
5. The user program can process the response.
6. Go to step 1 and repeat the cycle.

## Polling architecture: slave

The typical sequence for a slave is as follows:

1. The user program executes the Receive\_P2P instruction every scan.
2. When the CM or CB has received a request, the Receive\_P2P instruction indicates that new data is ready and the request is copied into the CPU.
3. The user program services the request and generates a response.
4. Use a Send\_P2P instruction to send the response back to the master.
5. Repeatedly execute Send\_P2P to be sure the transmit occurs.
6. Go to step 1 and repeat the cycle.

The slave must be responsible for calling Receive\_P2P frequently enough to receive a transmission from the master before the master times out while waiting for a response. To accomplish this task, the user program can call RCV\_PTP from a cyclic OB, where the cycle time is sufficient to receive a transmission from the master before the timeout period expires. If you set the cycle time for the OB to provide for two executions within the timeout period of the master, the user program can receive transmissions without missing any.

---

### Example: Point-to-Point communication


---

#### Example: Point-to-Point communication

In this example, an S7-1200 CPU communicates to a PC with a terminal emulator through a CM 1241 RS232 module. The point-to-point configuration and STEP 7 program in this example illustrate how the CPU can receive a message from the PC and echo the message back to the PC.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/Pb4oFoFkOjHpJ7J1s11Opw-VBkTPlmjVZAl17lebjV9hA/content?v=63cce1ab03319e8e)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/Pb4oFoFkOjHpJ7J1s11Opw-VBkTPlmjVZAl17lebjV9hA)

You must connect the communication interface of the CM 1241 RS232 module to the RS232 interface of the PC, which is normally COM1. Because both of these ports are Data Terminal Equipment (DTE), you must switch the receive and transmit pins (2 and 3) when connecting the two ports, which you can accomplish by either of the following methods:

- Use a NULL modem adapter to swap pins 2 and 3 together with a standard RS232 cable.
- Use a NULL modem cable, which already has pins 2 and 3 swapped. You can usually identify a NULL modem cable as one with two female 9-pin D connector ends.

---

#### Configuring the communication module

You can configure the CM 1241 from the Device configuration in STEP 7 or with user program instructions. This example uses the Device configuration method.

- Port configuration: Click the communication port of the CM module from the Device configuration, and configure the port as shown:

  [![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/oJOEXEyCUCmI1SmGLmhNSQ-VBkTPlmjVZAl17lebjV9hA/content?v=dfdf7b914cd2fbc8)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/oJOEXEyCUCmI1SmGLmhNSQ-VBkTPlmjVZAl17lebjV9hA)

  Note:

  The configuration settings for the CM 1241 (RS422/RS485) module include "Operating mode", "Receive line initial state", and "Wire break" as shown below. Refer to [Configuring the RS422 and RS485](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/z2DQv8aOnPrGUrjj2EoH3g?section=Xcf10950ce9a48e51c9daa1d34fd4b1bd).

  [![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/IXU0glkNe3KdhBrzZG7jnQ-VBkTPlmjVZAl17lebjV9hA/content?v=4ee2693a8c2bc796)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/IXU0glkNe3KdhBrzZG7jnQ-VBkTPlmjVZAl17lebjV9hA)
- Transmit message configuration: Accept the default for transmit message configuration. No break is to be sent at message start.
- Receive message start configuration: Configure the CM 1241 to start receiving a message when the communication line is inactive for at least 50 bit times (about 5 milliseconds at 9600 baud = 50 \* 1/9600):

  [![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/8NVeoxc72qDbccP4SRxsoA-VBkTPlmjVZAl17lebjV9hA/content?v=d6e2e0b985067a0e)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/8NVeoxc72qDbccP4SRxsoA-VBkTPlmjVZAl17lebjV9hA)
- Receive message end configuration: Configure the CM 1241 to end a message when it receives a maximum of 100 bytes or a linefeed character (10 decimal or a hexadecimal). The end sequence allows up to five end characters in sequence. The fifth character in the sequence is the linefeed character. The preceding four end sequence characters are "don’t care" or unselected characters. The CM 1241 does not evaluate the "don’t care" characters but looks for a linefeed character preceded by zero or more "don’t care" characters to indicate the message end.

  [![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/u8tvTdLmDiui4xnW0vuAIw-VBkTPlmjVZAl17lebjV9hA/content?v=e2272ea868b1b1fb)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/u8tvTdLmDiui4xnW0vuAIw-VBkTPlmjVZAl17lebjV9hA)

  [![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/UDHfYB25MLgkJHQsaIJtPw-VBkTPlmjVZAl17lebjV9hA/content?v=790604cb0528453f)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/UDHfYB25MLgkJHQsaIJtPw-VBkTPlmjVZAl17lebjV9hA)

  Receive buffer: Configure the number of received messages that the module will queue, stop the module from receiving more messages once the queue is full, and clear all previously received messages on a stop to run (startup) transition.

  Note:

  **Receive buffer settings**

  The receive buffer settings are only available for CM 1241 (RS232) and CM 1241 (RS422/485) with V2.1.

  [![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/bmbtIIbRAlGqCuNXJ~tKCw-VBkTPlmjVZAl17lebjV9hA/content?v=f116a548fbfa1fd3)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/bmbtIIbRAlGqCuNXJ~tKCw-VBkTPlmjVZAl17lebjV9hA)

---

#### RS422 and RS485 operating modes

## Configuring the RS422

For RS422 mode, there are three operating modes depending on your network configuration. Select one of these operating modes based on the devices in your network. The different selections for Receive line initial state reference the cases shown below for more details.

- Full duplex (RS422) four wire mode (point-to-point connection): select this option when there are two devices on your network. In the Receive line initial state:

  - Select none when you supply the bias and termination (Case 3).
  - Select forward bias to use internal bias and termination (Case 2).
  - Select reverse bias to use internal bias and termination, and enable cable break detection for both devices (Case 1).
- Full duplex (RS422) four wire mode (multipoint master): select this option for the master device when you have a network with one master and multiple slaves. In the Receive line initial state:

  - Select none when you supply the bias and termination (Case 3).
  - Select forward bias to use internal bias and termination (Case 2).
  - Cable break detection is not possible in this mode.
- Full duplex (RS422) four wire mode (multipoint slave): Select this option for all the slave devices when you have a network with one master and multiple slaves. In the Receive line initial state:

  - Select none when you supply the bias and termination (Case 3).
  - Select forward bias to use internal bias and termination (Case 2).
  - Select reverse bias to use internal bias and termination, and enable cable break detection for the slaves (Case 1).

## Case 1: RS422 with cable break detection

- Mode of operation: RS422
- Receive line initial state: Reverse bias (biased with R(A) > R(B) > 0V)
- Cable break: Cable break detection enabled (transmitter always active)

|  |  |
| --- | --- |
|  |  |

## Case 2: RS422 No cable break detection, forward bias

- Mode of operation: RS422
- Receive line initial state: Forward bias (biased with R(B) > R(A) > 0 V)
- Cable break: No cable break detection (transmitter enabled only while transmitting)

|  |  |
| --- | --- |
|  |  |

## Case 3: RS422: No cable break detection, no bias

- Mode of operation: RS422
- Receive line initial state: no bias
- Cable break: No cable break detection (transmitter enabled only while transmitting)

Bias and termination are added by the user at the end nodes of the network.

|  |  |
| --- | --- |
|  |  |

## Configuring the RS485

For RS485 mode, there is only one operating mode. The different selections for Receive line initial state reference the cases shown below for more details.

- Half duplex (RS485) two wire mode. In the Receive line initial state:

  - Select none when you supply the bias and termination (Case 5).
  - Select forward bias to use internal bias and termination (Case 4).

## Case 4: RS485: Forward bias

- Mode of operation: RS485
- Receive line initial state: Forward bias (biased with R(B) > R(A) > 0 V)

|  |  |
| --- | --- |
|  |  |

## Case 5: RS485: No bias (external bias)

- Mode of operation: RS485
- Receive line initial state: No bias (external bias required)

|  |  |
| --- | --- |
|  |  |

---

#### Programming the STEP 7 program

The example program uses a global data block for the communication buffer, a [RCV\_PTP instruction](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/OYyl3uL58luPjKF78BA8Iw?section=Xcac2c6c201a4abfd995ba47b35bd8b19) to receive data from the terminal emulator, and a [SEND\_PTP instruction](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/3zhF1GPWAOUV11cw83Dthg?section=Xc9a6126464345dd043cd773a9d0f5067) to echo the buffer back to the terminal emulator. To program the example, add the data block configuration and Main program block OB 1 as described below.

**Global data block "Comm\_Buffer":** Create a global data block (DB) and name it "Comm\_Buffer". Create one value in the data block called "buffer" with a data type of "array [0 .. 99] of byte".

**Network 1:** Enable the RCV\_PTP instruction whenever SEND\_PTP is not active. Tag\_8 at MW20.0 indicates when sending is complete in Network 4, and when the communication module is thus ready to receive a message.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/FvT_xWqqwhjVqi7xbx9uBA-VBkTPlmjVZAl17lebjV9hA/content?v=7e19c1a89d482198)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/FvT_xWqqwhjVqi7xbx9uBA-VBkTPlmjVZAl17lebjV9hA)

**Network 2:** Use the NDR value (Tag\_1 at M0.0) set by the RCV\_PTP instruction to make a copy of the number of bytes received and to set a flag (Tag\_8 at M20.0) to trigger the SEND\_PTP instruction.

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/vupOrwB8jG3YlttAteZ52g-VBkTPlmjVZAl17lebjV9hA)

**Network 3:** Enable the SEND\_PTP instruction when the M20.0 flag is set. Also use this flag to set the REQ input to TRUE for one scan. The REQ input tells the SEND\_PTP instruction that a new request is to be transmitted. The REQ input must only be set to TRUE for one execution of SEND\_PTP. The SEND\_PTP instruction is executed every scan until the transmit completes. The transmit is complete when the last byte of the message has been transmitted from the CM 1241. When the transmit is complete, the DONE output (Tag\_5 at M10.0) is set TRUE for one execution of SEND\_PTP.

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/ODtPEkrVHJrgnfTAkN_y0w-VBkTPlmjVZAl17lebjV9hA)

**Network 4:** monitor the DONE output of SEND\_PTP and reset the transmit flag (Tag\_8 at M20.0) when the transmit operation is complete. When the transmit flag is reset, the RCV\_PTP instruction in Network 1 is enabled to receive the next message.

[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/1m42dT6AGQzAW8Zl_vXn7g-VBkTPlmjVZAl17lebjV9hA)

---

#### Configuring the terminal emulator

You must set up the terminal emulator to support the example program. You can use most any terminal emulator on your PC, such as HyperTerminal. Make sure that the terminal emulator is in the disconnected mode before editing the settings as follows:

1. Set the terminal emulator to use the RS232 port on the PC (normally COM1).
2. Configure the port for 9600 baud, 8 data bits, no parity (none), 1 stop bit and no flow control.
3. Change the settings of the terminal emulator to emulate an ANSI terminal.
4. Configure the terminal emulator ASCII setup to send a line feed after every line (after the user presses the Enter key).
5. Echo the characters locally so that the terminal emulator displays what is typed.

---

#### Running the example program

To exercise the example program, follow these steps:

1. Download the STEP 7 program to the CPU and ensure that it is in RUN mode.
2. Click the "connect" button on the terminal emulator to apply the configuration changes and open a terminal session to the CM 1241.
3. Type characters at the PC and press Enter.

The terminal emulator sends the characters to the CM 1241 and to the CPU. The CPU program then echoes the characters back to the terminal emulator.

---

## Universal serial interface (USS) communication


---

### Overview

The USS instructions control the operation of motor drives which support the universal serial interface (USS) protocol. You can use the USS instructions to communicate with multiple drives through RS485 connections to CM 1241 RS485 communication modules or a CB 1241 RS485 communication board. Up to three CM 1241 RS422/RS485 modules and one CB 1241 RS485 board can be installed in a S7-1200 CPU. Each RS485 port can operate up to sixteen drives.

The USS protocol uses a master-slave network for communications over a serial bus. The master uses an address parameter to send a message to a selected slave. A slave itself can never transmit without first receiving a request to do so. Direct message transfer between the individual slaves is not possible. USS communication operates in half-duplex mode. The following USS illustration shows a network diagram for an example drive application.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/JSqJjUH_o6eZyVKmumZ~Fg-VBkTPlmjVZAl17lebjV9hA/content?v=eaf8b4a12f5f771e)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/JSqJjUH_o6eZyVKmumZ~Fg-VBkTPlmjVZAl17lebjV9hA)

## USS communications through PROFIBUS or PROFINET

USS communication enables you to use a PROFINET or PROFIBUS distributed I/O rack to communicate to various devices (RFID readers, GPS device, and others):

- [PROFINET](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Z44~rg1h4WN9JoB7bugZXQ?section=Xa4efc1a7d4610374ba647f805029a400): You connect the Ethernet interface of the S7-1200 CPU to a PROFINET interface module. PtP communication modules in the rack with the interface module can then provide serial communications to USS drives.
- [PROFIBUS](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/bUmtrcn0SdnXwmyXWr7~qA?section=X857a761a79879d39777112eb0d337413): You insert a PROFIBUS communication module in the left side of the rack with the S7-1200 CPU. You connect the PROFIBUS communication module to a rack containing a PROFIBUS interface module. PtP communication modules in the rack with the interface module can then provide serial communications to USS drives.

The S7-1200 supports two sets of USS instructions:

- [USS instructions](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/I4RZoxXufmRGQYVJ18z27w?section=X2fe52efe4d7d6da3062a82e1b1d9309e): These USS instructions provide all of the functionality of the legacy instructions, plus the ability to connect to PROFINET and PROFIBUS distributed I/O. These USS instructions allow you to configure the communications between the PtP communication modules in the distributed I/O rack and the USS drives. S7‑1200 CM 1241 modules must have a minimum firmware version of V2.1 to use these USS instructions.
- [Legacy USS instructions](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/b20dJlTjCu_XJHXQWg1SYQ?section=X3983558f793c20a2f75cf2cbb558f5fc): These USS instructions existed prior to version V4.0 of the S7-1200 and only work with serial communications using a CM 1241 communication module or CB 1241 communication board.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/ilH0NFaOymnDPi4FzDxdnQ-VBkTPlmjVZAl17lebjV9hA/content?v=5b808121012d5027)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/ilH0NFaOymnDPi4FzDxdnQ-VBkTPlmjVZAl17lebjV9hA)

|  |  |
| --- | --- |
|  | The blue arrows indicate the flow of bidirectional communication between devices. |

Note that STEP 7 provides different versions of the USS instructions. For information on instruction versions, refer to [Use Instruction versions](https://support.industry.siemens.com/cs/ww/en/view/109798671/113722878475) in the STEP 7 Information System.

## Requirements for using the USS protocol

The four USS instructions use two FBs and two FCs to support the USS protocol. For each USS network, one instance data block (DB) is used for USS\_Port\_Scan and one instance data block for all calls of USS\_Drive\_Control. For further requirements, refer to the topic "[Requirements for using the USS protocol](https://support.industry.siemens.com/cs/ww/en/view/109798671/140076559243)" in the STEP 7 Information System.

---

### USS instructions


---

#### USS_Port_Scan (Edit communication using USS network)

Table 1. USS\_Port\_Scan instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **USS\_Port\_Scan(    PORT:=\_uint\_in\_,    BAUD:=\_dint\_in\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    USS\_DB:=\_fbtref\_inout\_);** | The USS\_Port\_Scan instruction handles communication over a USS network. |

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| PORT | IN | Port | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. |
| BAUD | IN | DInt | The baud rate used for USS communication. |
| USS\_DB | INOUT | USS\_BASE | The name of the instance DB that is created and initialized when a USS\_Drive\_Control instruction is placed in your program. |
| ERROR | OUT | Bool | When true, this output indicates that an error has occurred and the STATUS output is valid. |
| STATUS | OUT | Word | The status value of the request indicates the result of the scan or initialization. Additional information is available in the "USS\_Extended\_Error" variable for some status codes. |

Typically, there is only one USS\_Port\_Scan instruction per PtP communication port in the program, and each call of this Function Block (FB) handles a transmission to or from a single drive. All USS functions associated with one USS network and PtP communication port must use the same instance DB.

Your program must execute the USS\_Port\_Scan instruction often enough to prevent drive timeouts. USS\_Port\_Scan is usually called from a cyclic interrupt OB to prevent drive timeouts and keep the most recent USS data updates available for USS\_Drive\_Control calls.

Note:

When using the USS protocol library and the USS\_Port\_Scan instruction with a CB 1241, you must set the LINE\_PRE data block tag to a value of 0 (No initial state). The default value of 2 for the LINE\_PRE data block tag results in an error value of 16#81AB being returned by the USS\_Port\_Scan instruction. The LINE\_PRE data block tag is found in the data block associated with the USS\_Port\_Scan instruction (usually named USS\_Port\_Scan\_DB).

Ensure the start value of LINE\_PRE is changed to a 0 (zero).

---

#### USS_Drive_Control (Swap data with drive)

Table 1. USS\_Drive\_Control instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"USS\_Drive\_Control\_DB"(    RUN:=\_bool\_in\_,    OFF2:=\_bool\_in\_,    OFF3:=\_bool\_in\_,    F\_ACK:=\_bool\_in\_,    DIR:=\_bool\_in\_,    DRIVE:=\_usint\_in\_,    PZD\_LEN:=\_usint\_in\_,    SPEED\_SP:=\_real\_in\_,    CTRL3:=\_word\_in\_,    CTRL4:=\_word\_in\_,    CTRL5:=\_word\_in\_,    CTRL6:=\_word\_in\_,    CTRL7:=\_word\_in\_,    CTRL8:=\_word\_in\_,    NDR=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    RUN\_EN=>\_bool\_out\_,    D\_DIR=>\_bool\_out\_,    INHIBIT=>\_bool\_out\_,    FAULT=>\_bool\_out\_,    SPEED=>\_real\_out\_,    STATUS1=>\_word\_out\_,    STATUS3=>\_word\_out\_,    STATUS4=>\_word\_out\_,    STATUS5=>\_word\_out\_,    STATUS6=>\_word\_out\_,    STATUS7=>\_word\_out\_,    STATUS8=>\_word\_out\_);** | The USS\_Drive\_Control instruction exchanges data with a drive by creating request messages and interpreting the drive response messages. A separate function block should be used for each drive, but all USS functions associated with one USS network and PtP communication port must use the same instance data block. You must create the DB name when you place the first USS\_Drive\_Control instruction and then reference the DB that was created by the initial instruction usage.  STEP 7 automatically creates the DB when you insert the instruction. |

1 LAD and FBD: Expand the box to reveal all the parameters by clicking the bottom of the box. The parameter pins that are grayed are optional and parameter assignment is not required.

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| RUN | IN | Bool | Drive start bit: When true, this input enables the drive to run at the preset speed. When RUN goes to false while a drive is running, the motor will be ramped down to a stop. This behavior differs from the dropping power (OFF2) or braking the motor (OFF3). |
| OFF2 | IN | Bool | Electrical stop bit: When false, this bit causes the drive to coast to a stop with no braking. |
| OFF3 | IN | Bool | Fast stop bit: When false, this bit causes a fast stop by braking the drive rather than just allowing the drive to coast to a stop. |
| F\_ACK | IN | Bool | Fault acknowledge bit: This bit is set to reset the fault bit on a drive. The bit is set after the fault is cleared to indicate to the drive it no longer needs to indicate the previous fault. |
| DIR | IN | Bool | Drive direction control: This bit is set to indicate that the direction is forward (for positive SPEED\_SP). |
| DRIVE | IN | USInt | Drive address: This input is the address of the USS drive. The valid range is drive 1 to drive 16. |
| PZD\_LEN | IN | USInt | Word length: This is the number of words of PZD data. The valid values are 2, 4, 6, or 8 words. The default value is 2. |
| SPEED\_SP | IN | Real | Speed set point: This is the speed of the drive as a percentage of configured frequency. A positive value specifies forward direction (when DIR is true). Valid range is 200.00 to -200.00. |
| CTRL3 | IN | Word | Control word 3: A value written to a user-configurable parameter on the drive. You must configure this on the drive. (optional parameter) |
| CTRL4 | IN | Word | Control word 4: A value written to a user-configurable parameter on the drive. You must configure this on the drive. (optional parameter) |
| CTRL5 | IN | Word | Control word 5: A value written to a user-configurable parameter on the drive. You must configure this on the drive. (optional parameter) |
| CTRL6 | IN | Word | Control word 6: A value written to a user-configurable parameter on the drive. You must configure this on the drive. (optional parameter) |
| CTRL7 | IN | Word | Control word 7: A value written to a user-configurable parameter on the drive. You must configure this on the drive. (optional parameter) |
| CTRL8 | IN | Word | Control word 8: A value written to a user-configurable parameter on the drive. You must configure this on the drive. (optional parameter) |
| NDR | OUT | Bool | New data ready: When true, the bit indicates that the outputs contain data from a new communication request. |
| ERROR | OUT | Bool | Error occurred: When true, this indicates that an error has occurred and the STATUS output is valid. All other outputs are set to zero on an error. Communication errors are only reported on the USS\_Port\_Scan instruction ERROR and STATUS outputs. |
| STATUS | OUT | Word | The status value of the request indicates the result of the scan. This is not a status word returned from the drive. |
| RUN\_EN | OUT | Bool | Run enabled: This bit indicates whether the drive is running. |
| D\_DIR | OUT | Bool | Drive direction: This bit indicates whether the drive is running forward. |
| INHIBIT | OUT | Bool | Drive inhibited: This bit indicates the state of the inhibit bit on the drive. |
| FAULT | OUT | Bool | Drive fault: This bit indicates that the drive has registered a fault. You must fix the problem and then set the F\_ACK bit to clear this bit when set. |
| SPEED | OUT | Real | Drive Current Speed (scaled value of drive status word 2): The value of the speed of the drive as a percentage of configured speed. |
| STATUS1 | OUT | Word | Drive Status Word 1: This value contains fixed status bits of a drive. |
| STATUS3 | OUT | Word | Drive Status Word 3: This value contains a user-configurable status word on the drive. |
| STATUS4 | OUT | Word | Drive Status Word 4: This value contains a user-configurable status word on the drive. |
| STATUS5 | OUT | Word | Drive Status Word 5: This value contains a user-configurable status word on the drive. |
| STATUS6 | OUT | Word | Drive Status Word 6: This value contains a user-configurable status word on the drive. |
| STATUS7 | OUT | Word | Drive Status Word 7: This value contains a user-configurable status word on the drive. |
| STATUS8 | OUT | Word | Drive Status Word 8: This value contains a user-configurable status word on the drive. |

When the initial USS\_Drive\_Control execution occurs, the drive indicated by the USS address (parameter DRIVE) is initialized in the Instance DB. After this initialization, subsequent executions of USS\_Port\_Scan can begin communication to the drive at this drive number.

Changing the drive number requires a CPU STOP-to-RUN mode transition that initializes the instance DB. Input parameters are configured into the USS TX message buffer and outputs are read from a "previous" valid response buffer if any exists. There is no data transmission during USS\_Drive\_Control execution. Drives communicate when USS\_Port\_Scan is executed. USS\_Drive\_Control only configures the messages to be sent and interprets data that might have been received from a previous request.

You can control the drive direction of rotation using either the DIR input (Bool) or using the sign (positive or negative) with the SPEED\_SP input (Real). The following table indicates how these inputs work together to determine the drive direction, assuming the motor is wired for forward rotation.

Table 3. Interaction of the SPEED\_SP and DIR parameters

| **SPEED\_SP** | **DIR** | **Drive rotation direction** |
| --- | --- | --- |
| Value > 0 | 0 | Reverse |
| Value > 0 | 1 | Forward |
| Value < 0 | 0 | Forward |
| Value < 0 | 1 | Reverse |

---

#### USS_Read_Param (Readout parameters from the drive)

Table 1. USS\_Read\_Param instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **USS\_Read\_Param(REQ:=\_bool\_in\_,    DRIVE:=\_usint\_in\_,    PARAM:=\_uint\_in\_,    INDEX:=\_uint\_in\_,    DONE=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    VALUE=>\_variant\_out\_,    USS\_DB:=\_fbtref\_inout\_);** | The USS\_Read\_Param instruction reads a parameter from a drive. All USS functions associated with one USS network and PtP communication port must use the same data block. USS\_Read\_Param must be called from a main program cycle OB. |

Table 2. Data types for the parameters

| **Parameter type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Send request: When true, REQ indicates that a new read request is desired. This is ignored if the request for this parameter is already pending. |
| DRIVE | IN | USInt | Drive address: DRIVE is the address of the USS drive. The valid range is drive 1 to drive 16. |
| PARAM | IN | UInt | Parameter number: PARAM designates which drive parameter is written. The range of this parameter is 0 to 2047. On some drives, the most significant byte can access PARAM values greater than 2047. See your drive manual for details on how to access an extended range. |
| INDEX | IN | UInt | Parameter index: INDEX designates which Drive Parameter index is to be written. A 16-bit value where the Least Significant Byte is the actual index value with a range of (0 to 255). The Most Significant Byte may also be used by the drive and is drive-specific. See your drive manual for details. |
| USS\_DB | INOUT | USS\_BASE | The name of the instance DB that is created and initialized when a USS\_Drive\_Control instruction is placed in your program. |
| VALUE | IN | Word, Int, UInt, DWord, DInt, UDInt, Real | This is the value of the parameter that was read and is valid only when the DONE bit is true. |
| DONE1 | OUT | Bool | When true, indicates that the VALUE output holds the previously requested read parameter value. This bit is set when USS\_Drive\_Control sees the read response data from the drive. This bit is reset when either: you request the response data using another USS\_Read\_Param poll, or on the second of the next two calls to USS\_Drive\_Control. |
| ERROR | OUT | Bool | Error occurred: When true, ERROR indicates that an error has occurred and the STATUS output is valid. All other outputs are set to zero on an error. Communication errors are only reported on the USS\_Port\_Scan instruction ERROR and STATUS outputs. |
| STATUS | OUT | Word | STATUS indicates the result of the read request. Additional information is available in the "USS\_Extended\_Error" variable for some status codes. |

1 The DONE bit indicates that valid data has been read from the referenced motor drive and delivered to the CPU. It does not indicate that the USS library is capable of immediately reading another parameter. A blank PKW request must be sent to the motor drive and must also be acknowledged by the instruction before the parameter channel for the specific drive becomes available for use. Immediately calling a USS\_Read\_Param or USS\_Write\_Param FC for the specified motor drive will result in a "0x818A" error.

---

#### USS_Write_Param (Change parameters in the drive)

Note:

**EEPROM write operations (for the EEPROM inside a USS drive)**

Do not overuse the EEPROM permanent write operation. Minimize the number of EEPROM write operations to extend the EEPROM life.

Table 1. USS\_Write\_Param instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **USS\_Write\_Param(REQ:=\_bool\_in\_,    DRIVE:=\_usint\_in\_,    PARAM:=\_uint\_in\_,    INDEX:=\_uint\_in\_,    EEPROM:=\_bool\_in\_,    VALUE:=\_variant\_in\_,    DONE=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    USS\_DB:=\_fbtref\_inout\_);** | The USS\_Write\_Param instruction modifies a parameter in the drive. All USS functions associated with one USS network and PtP communication port must use the same data block.  USS\_Write\_Param must be called from a main program cycle OB. |

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Send request: When true, REQ indicates that a new write request is desired. This is ignored if the request for this parameter is already pending. |
| DRIVE | IN | USInt | Drive address: DRIVE is the address of the USS drive. The valid range is drive 1 to drive 16. |
| PARAM | IN | UInt | Parameter number: PARAM designates which drive parameter is written. The range of this parameter is 0 to 2047. On some drives, the most significant byte can access PARAM values greater than 2047. See your drive manual for details on how to access an extended range. |
| INDEX | IN | UInt | Parameter index: INDEX designates which Drive Parameter index is to be written. A 16-bit value where the least significant byte is the actual index value with a range of (0 to 255). The most significant byte may also be used by the drive and is drive-specific. See your drive manual for details. |
| EEPROM | IN | Bool | Store To Drive EEPROM: When true, a write drive parameter transaction will be stored in the drive EEPROM. If false, the write is temporary and will not be retained if the drive is power cycled. |
| VALUE | IN | Word, Int, UInt, DWord, DInt, UDInt, Real | The value of the parameter that is to be written. It must be valid on the transition of REQ. |
| USS\_DB | INOUT | USS\_BASE | The name of the instance DB that is created and initialized when a USS\_Drive\_Control instruction is placed in your program. |
| DONE1 | OUT | Bool | When true, DONE indicates that the input VALUE has been written to the drive. This bit is set when USS\_Drive\_Control sees the write response data from the drive. This bit is reset when either you request the response data using another USS\_Drive\_Control poll, or on the second of the next two calls to USS\_Drive\_Control. |
| ERROR | OUT | Bool | When true, ERROR indicates that an error has occurred and the STATUS output is valid. All other outputs are set to zero on an error. Communication errors are only reported on the USS\_Port\_Scan instruction ERROR and STATUS outputs. |
| STATUS | OUT | Word | STATUS indicates the result of the write request. Additional information is available in the "USS\_Extended\_Error" variable for some status codes. |

1 The DONE bit indicates that valid data has been read from the referenced motor drive and delivered to the CPU. It does not indicate that the USS library is capable of immediately reading another parameter. A blank PKW request must be sent to the motor drive and must also be acknowledged by the instruction before the parameter channel for the specific drive becomes available for use. Immediately calling a USS\_Read\_Param or USS\_Write\_Param FC for the specified motor drive will result in a "0x818A" error.

---

### USS status codes

USS instruction status codes are returned at the STATUS output of the USS functions.

Table 1. STATUS codes 1

| **STATUS (W#16#....)** | **Description** |
| --- | --- |
| 0000 | No error |
| 8180 | The length of the drive response did not match the characters received from the drive. The drive number where the error occurred is returned in the "USS\_Extended\_Error" variable. See the extended error description below this table. |
| 8181 | VALUE parameter was not a Word, Real or DWord data type. |
| 8182 | The user supplied a Word for a parameter value and received a DWord or Real from the drive in the response. |
| 8183 | The user supplied a DWord or Real for a parameter value and received a Word from the drive in the response. |
| 8184 | The response telegram from drive had a bad checksum. The drive number where the error occurred is returned in the "USS\_Extended\_Error" variable. See the extended error description below this table. |
| 8185 | Illegal drive address (valid drive address range: 1 to16) |
| 8186 | The speed set point is out of the valid range (valid speed SP range: -200% to 200%). |
| 8187 | The wrong drive number responded to the request sent. The drive number where the error occurred is returned in the "USS\_Extended\_Error" variable. See the extended error description below this table. |
| 8188 | Illegal PZD word length specified (valid range = 2, 4, 6 or 8 words) |
| 8189 | Illegal Baud Rate was specified. |
| 818A | The parameter request channel is in use by another request for this drive. |
| 818B | The drive has not responded to requests and retries. The drive number where the error occurred is returned in the "USS\_Extended\_Error" variable. See the extended error description below this table. |
| 818C | The drive returned an extended error on a parameter request operation. See the extended error description below this table. |
| 818D | The drive returned an illegal access error on a parameter request operation. See your drive manual for information of why parameter access may be limited. |
| 818E | The drive has not been initialized. This error code is returned to USS\_Read\_Param or USS\_Write\_Param when USS\_Drive\_Control, for that drive, has not been called at least once. This keeps the initialization on first scan of USS\_Drive\_Control from overwriting a pending parameter read or write request, since it initializes the drive as a new entry. To fix this error, call USS\_Drive\_Control for this drive number. |
| 80Ax-80Fx | Specific errors returned from PtP communication FBs called by the USS Library - These error code values are not modified by the USS library and are defined in the PtP instruction descriptions. |

1 In addition to the USS instruction errors listed above, errors can be returned from the underlying [PtP communication instructions](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/WokKup3hHE5TA5afrW71kw?section=X8ba04b7c52b04f768f2b30e665c08595).

For several STATUS codes, additional information is provided in the "USS\_Extended\_Error" variable of the USS\_Drive\_Control Instance DB. For STATUS codes hexadecimal 8180, 8184, 8187, and 818B, USS\_Extended\_Error contains the drive number where the communication error occurred. For STATUS code hexadecimal 818C, USS\_Extended\_Error contains a drive error code returned from the drive when using a USS\_Read\_Param or USS\_Write\_Param instruction.

## Example: Communication errors reporting

Communication errors (STATUS = 16#818B) are only reported on the USS\_Port\_Scan instruction and not on the USS\_Drive\_Control instruction. For example, if the network is not properly terminated, then it is possible for a drive to go to RUN but the USS\_Drive\_Control instruction will show all "0's' for the output parameters. In this case, you can only detect the communication error on the USS\_Port\_Scan instruction. Since this error is only visible for one scan, you will need to add some capture logic as illustrated in the following example. In this example, when the error bit of the USS\_Port\_Scan instruction is TRUE, then the STATUS and the USS\_Extended\_Error values are saved into M memory. The drive number is placed in the USS\_Extended\_Error variable when the STATUS code value is hexadecimal 8180, 8184, 8187, or 818B.

|  |  |
| --- | --- |
|  | **Network 1:** "PortStatus"port status and"USS\_Drive\_Control\_DB".USS\_Extended\_Error  extended error code values are only valid for  one program scan. The values must be  captured for later processing. |
|  | **Network 2**: The "PortError" contact triggers the storage of the "PortStatus" value in "LastPortStatus" and the"USS\_Drive\_Control\_DB".USS\_Extended\_Error  value in "LastExtError". |

## Read and write access to a drive's internal parameters

USS drives support read and write access to a drive's internal parameters. This feature allows remote control and configuration of the drive. Drive parameter access operations can fail due to errors such as values out of range or illegal requests for a drive's current mode. The drive generates an error code value that is returned in the "USS\_Extended\_Error" variable. This error code value is only valid for the last execution of a USS\_Read\_Param or USS\_Write\_Param instruction. The drive error code is put into USS\_Extended\_Error variable when the STATUS code value is hexadecimal 818C. The error code value of USS\_Extended\_Error depends on the drive model. See the drive's manual for a description of the extended error codes for read and write parameter operations.

---

### USS general drive setup requirements

USS general drive setup requirements consist of the following points:

- The drives must be set to use 4 PKW words.
- The drives can be configured for 2, 4, 6, or 8 PZD words.
- The number of PZD word's in the drive must match PZD\_LEN input on the USS\_Drive\_Control instruction for that drive.
- The baud rate in all the drives must match the BAUD input on the USS\_Port\_Scan instruction.
- The drive must be set for remote control.
- The drive must be set for frequency set-point to USS on COM Link.
- The drive address must be set to 1 to 16 and match the DRIVE input on the USS\_Drive\_Control block for that drive.
- The drive direction control must be set to use the polarity of the drive set-point.
- The RS485 network must be terminated properly.

---

### Example: USS general drive connection and setup

## Connecting a MicroMaster drive

This information about SIEMENS MicroMaster drives is provided as an example. For other drives, refer to the drive's manual for setup instructions.

To make the connection to a MicroMaster Series 4 (MM4) drive, insert the ends of the RS485 cable into the two caged-clamp, screw-less terminals provided for USS operation. Standard PROFIBUS cable and connectors can be used to connect the S7-1200.

CAUTION:

**Risks when interconnecting equipment with different reference potentials**

Interconnecting equipment with different reference potentials can cause unwanted currents to flow through the interconnecting cable. These unwanted currents can cause communications errors or damage equipment.

Be sure all equipment that you connect with a communications cable either shares a common circuit reference or is isolated to prevent unwanted current flows. The shield must be tied to the chassis ground or to pin 1 on the 9-pin connector. Tie the wiring terminal 2-0 V on the MicroMaster drive to the chassis ground.

Communications errors or damaged equipment can cause injury.

The two wires at the opposite end of the RS485 cable must be inserted into the MM4 drive terminal blocks. To make the cable connection on a MM4 drive, remove the drive cover(s) to access the terminal blocks. See the MM4 user manual for details about how to remove the covers(s) of your specific drive.

|  |  |
| --- | --- |
|  |  |
| The terminal block connections are labeled numerically. Using a PROFIBUS connector on the S7-1200 side, connect the A terminal of the cable to the drive terminal 15 (for an MM420) or terminal 30 (MM440). Connect the B terminal of B (P) A (N) the cable connector to terminal 14 (MM420) or terminal 29 (MM440).  If the S7-1200 is a terminating node in the network, or if the connection is point-to-point, it is necessary to use terminals A1 and B1 (not A2 and B2) of the connector since they allow the termination settings to be set (for example, with DP connector type 6ES7972-0BA40-0X40). | |

Warning:

**Risk of electric shock or electrocution**

Some drives have high voltages. Failure to replace drive covers properly can result in electric shock or electrocution.

Make sure the drive covers are replaced properly before supplying power to the unit.

Electric shock or electrocution can result in severe personal injury or death.

|  |  |
| --- | --- |
| If the drive is configured as the terminating node in the network, then termination and bias resistors must also be wired to the appropriate terminal connections. This diagram shows examples of the MM4 drive connections necessary for termination and bias. |  |

## Setting up the MM4 drive

Before you connect a drive to the S7-1200, you must ensure that the drive has the following system parameters. Use the keypad on the drive to set the parameters:

Table 1.

|  |  |
| --- | --- |
| 1. Reset the drive to factory settings (optional). | P0010=30  P0970=1 |
| If you skip step 1, then ensure that these parameters are set to the indicated values. | USS PZD length = P2012 Index 0=(2, 4, 6, or 8)  USS PKW length = P2013 Index 0=4 |
| 2. Enable the read/write access to all parameters (Expert mode). | P0003=3 |
| 3. Check the motor settings for your drive. The settings will vary according to the motor(s) being used.  To set the parameters P304, P305, P307, P310, and P311, you must first set parameter P010 to 1 (quick commissioning mode). When you are finished setting the parameters, set parameter P010 to 0. Parameters P304, P305, P307, P310, and P311 can only be changed in the quick commissioning mode. | P0304 = Rated motor voltage (V)  P0305 = Rated motor current (A)  P0307 = Rated motor power (W)  P0310 = Rated motor frequency (Hz)  P0311 = Rated motor speed |
| 4. Set the local/remote control mode. | P0700 Index 0=5 |
| 5. Set selection of frequency set-point to USS on COM link. | P1000 Index 0=5 |
| 6. Ramp up time (optional)  This is the time in seconds that it takes the motor to accelerate to maximum frequency. | P1120=(0 to 650.00) |
| 7. Ramp down time (optional)  This the time in seconds that it takes the motor to decelerate to a complete stop. | P1121=(0 to 650.00) |
| 8. Set the serial link reference frequency: | P2000=(1 to 650 Hz) |
| 9. Set the USS normalization: | P2009 Index 0=0 |
| 10. Set the baud rate of the RS485 serial interface: | P2010 Index 0= 4 (2400 baud)  5 (4800 baud)  6 (9600 baud)  7 (19200 baud  8 (38400 baud)  9 (57600 baud)  12 (115200 baud) |
| 11. Enter the Slave address.  Each drive (a maximum of 31) can be operated over the bus. | P2011 Index 0=(0 to 31) |
| 12. Set the serial link timeout.  This is the maximum permissible period between two incoming data telegrams. This feature is used to turn off the inverter in the event of a communications failure. Timing starts after a valid data telegram has been received. If a further data telegram is not received within the specified time period, the inverter will trip and display fault code F0070. Setting the value to zero switches off the control. | P2014 Index 0=(0 to 65,535 ms)  0=timeout disabled |
| 13. Transfer the data from RAM to EEPROM: | P0971=1 (Start transfer) Save the changes to the parameter settings to EEPROM |

---

## Modbus communication


---

### Overview of Modbus TCP and Modbus RTU communication

## Modbus function codes

- A CPU operating as a Modbus TCP client or Modbus RTU master can read/write both data and I/O states in a remote Modbus TCP server or Modbus RTU slave. Remote data can be read and then processed in your program logic.
- A CPU operating as a Modbus TCP server or Modbus RTU slave allows a supervisory device to read/write both data and I/O states in CPU memory. A Modbus TCP client or Modbus RTU master can write new values into slave/server CPU memory that is available to your program logic.

Warning:

**Avoiding security risks from physical network attacks**

If an attacker can physically access your networks, the attacker can possibly read and write data.

For example, I/O exchange through PROFIBUS, PROFINET, AS-i, or other I/O bus, GET/PUT, T-Block, and communication modules (CMs) have no security features. You must protect these forms of communication by limiting physical access. If an attacker can physically access your networks using these forms of communication, the attacker can possibly read and write data.

If you fail to protect these forms of communication, death or severe personal injury can result.

For security information and recommendations, see the "Operational Guidelines” white paper on the [Siemens Industrial Cybersecurity Web site](https://www.siemens.com/global/en/products/automation/topic-areas/industrial-cybersecurity.html).

Table 1. Read data functions: Read remote I/O and program data

| **Modbus function code** | **Read slave (server) functions - standard addressing** |
| --- | --- |
| 01 | Read output bits: 1 to 2000 bits per request |
| 02 | Read input bits: 1 to 2000 bits per request |
| 03 | Read Holding registers: 1 to 125 words per request |
| 04 | Read input words: 1 to 125 words per request |

Table 2. Write data functions: Write remote I/O and modify program data

| **Modbus function code** | **Write slave (server) functions - standard addressing** |
| --- | --- |
| 05 | Write one output bit: 1 bit per request |
| 06 | Write one holding register: 1 word per request |
| 15 | Write one or more output bits: 1 to 1968 bits per request |
| 16 | Write one or more holding registers: 1 to 123 words per request |

- Modbus function codes 08 and 11 provide slave device communication diagnostic information.
- Modbus function code 0 broadcasts a message to all slaves (with no slave response). The broadcast function is not available for Modbus TCP, because communication is connection based.
- Modbus function code 23 can Write and Read one or more holding registers: 1 to 121/125 (Write/Read) words per request. This function code is only available for Modbus TCP.

Table 3. Modbus network station addresses

| **Station** | | **Address** |
| --- | --- | --- |
| TCP station | Station address | IP address and port number |
| RTU station | Standard station address | 1 to 247 |
| Extended station address | 1 to 65535 |

## Modbus memory addresses

The actual number of Modbus memory addresses available depends on the CPU model, how much work memory exists, and how much CPU memory is used by other program data. The table below gives the nominal value of the address range.

Table 4. Modbus memory addresses

| **Station** | | **Address range** |
| --- | --- | --- |
| TCP station | Standard memory address | 10K |
| RTU station | Standard memory address | 10K |
| Extended memory address | 64K |

---

### Modbus TCP


---

#### Overview

Modbus TCP (Transmission Control Protocol) is a standard network communication protocol that uses the PROFINET connector on the CPU for TCP/IP communication. No additional communication hardware module is required.

Modbus TCP uses Open User Communications (OUC) connections as a Modbus communication path. Multiple client-server connections may exist in addition to the connection between STEP 7 and the CPU. Mixed client and server connections are supported up to the [maximum number of connections allowed by the CPU model](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/sLHuVdWZrv8gmzf1L~x4Ww?section=X0addf1af4d428dcab856741f6adb88fc).

Each MB\_SERVER connection must use a unique instance DB and IP port number. Only 1 connection per IP port is supported. Each MB\_SERVER (with its unique instance DB and IP port) must be executed individually for each connection.

A Modbus TCP client (master) must control the client-server connection with the DISCONNECT parameter. The basic Modbus client actions are shown below:

1. Initiate a connection to a particular server (slave) IP address and IP port number
2. Initiate client transmission of a Modbus message and receive the server responses
3. When desired, initiate the disconnection of client and server to enable connection with a different server.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/Ym7t8rWKmPE8JcWaawogng-VBkTPlmjVZAl17lebjV9hA/content?v=85fd4155e815648b)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/Ym7t8rWKmPE8JcWaawogng-VBkTPlmjVZAl17lebjV9hA)

## Modbus TCP instructions and versions

The [Modbus TCP instructions](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/DgcT6tn9xvpm0UZhh8HKFA?section=X88fc3be69ed9f9cdd357672d8ac2a247) provide the capability to communicate between Modbus TCP clients, Modbus TCP servers, and third-party Modbus TCP devices through a switch. Older S7-1200 programs might use [Legacy Modbus TCP instructions.](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/XqUv7OQjOB8sfHhhJdJcwg?section=X401f833624d5e5de2d3770bde4f8c01b)

STEP 7 provides different versions of the Modbus TCP instructions. For information on instruction versions, refer to [Use Instruction versions](https://support.industry.siemens.com/cs/ww/en/view/109798671/113722878475) in the STEP 7 Information System.

---

#### Modbus TCP instructions


---

##### MB_CLIENT (Communicate using PROFINET as Modbus TCP client) instruction

Table 1. MB\_CLIENT instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"MB\_CLIENT\_DB"( REQ:=\_bool\_in\_, DISCONNECT:=\_bool\_in\_, MB\_MODE:=\_usint\_in\_, MB\_DATA\_ADDR:=\_udint\_in\_, MB\_DATA\_LEN:=\_uint\_in\_, RD\_MB\_DATA\_ADDR:=\_uint\_in\_, RD\_MB\_DATA\_LEN:=\_uint\_in\_, WR\_MB\_DATA\_ADDR:=\_uint\_in\_, WR\_MB\_DATA\_LEN:=\_uint\_in\_, DONE=>\_bool\_out\_, BUSY=>\_bool\_out\_, ERROR=>\_bool\_out\_, STATUS=>\_word\_out\_, MB\_DATA\_PTR:=\_variant\_inout\_, CONNECT:=\_variant\_inout\_, RD\_MB\_DATA\_PTR:=\_variant\_inout\_, WR\_MB\_DATA\_PTR:**  **=\_variant\_inout\_**); | MB\_CLIENT communicates as a Modbus TCP client through the PROFINET port on the S7-1200 CPU. No additional communication hardware module is required.MB\_CLIENT can make a client-server connection, send a Modbus function request, receive a response, and control the disconnection from a Modbus TCP server. |

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | In | Bool | FALSE = No Modbus communication request  TRUE = Request to communicate with a Modbus TCP server |
| DISCONNECT | IN | Bool | The DISCONNECT parameter allows your program to control connection and disconnection with a Modbus server device.  If DISCONNECT = 0 and a connection does not exist, then MB\_CLIENT attempts to make a connection to the assigned IP address and port number.  If DISCONNECT = 1 and a connection exists, then a disconnect operation is attempted. Whenever this input is enabled, no other operation will be attempted. |
| MB\_MODE | IN | USInt | Mode selection: Assigns the type of request (read, write, or diagnostic). See the Modbus functions table below for details. |
| MB\_DATA\_ADDR | IN | UDInt | Modbus starting Address: Assigns the starting address of the data to be accessed by MB\_CLIENT. See the following Modbus functions table for valid addresses. |
| MB\_DATA\_LEN | IN | UInt | Modbus data Length: Assigns the number of bits or words to be accessed in this request. See the following Modbus functions table for valid lengths |
| MB\_DATA\_PTR | IN\_OUT | Variant | Pointer to the Modbus data register: The register buffers data going to or coming from a Modbus server. The pointer must assign a non-optimized global DB or an M memory address. |
| CONNECT | IN\_OUT | Variant | Reference to a Data block structure that contains connection parameters in the system data type "TCON\_IP\_v4". The following data types are also supported: TCON\_IP\_V4\_SEC, TCON\_QDN and TCON\_QDN\_SEC. See  ["Parameters for the PROFINET connection"](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/4KPJfLxRtqynTXLM0pgSaQ?section=X868ef9f6da288ebcc92dd27a15c9077b). |
| DONE | OUT | Bool | The DONE bit is TRUE for one scan, after the last request was completed with no error. |
| BUSY | OUT | Bool | - 0 - No MB\_CLIENT operation in progress - 1 - MB\_CLIENT operation in progress |
| ERROR | OUT | Bool | The ERROR bit is TRUE for one scan, after the MB\_CLIENT execution ended with an error. The error code at the STATUS parameter is valid only during the single cycle where ERROR = TRUE. |
| STATUS | OUT | Word | Execution condition code |

## Modbus function 23

**Description**

With the Modbus function 23, the following is carried out in a job:

1. Data is transferred from the CPU to the Modbus server and written into one or more holding registers.
2. Data is read from one or more holding registers of the Modbus server and transferred to the CPU.

The "MB\_CLIENT" instruction supports the Modbus function 23 as of instruction version V6.0.

**Parameters**

When the Modbus function 23 is used, the MB\_MODE parameter must have the value 123.

The parameters MB\_DATA\_ADDR, MB\_DATA\_LEN and MB\_DATA\_PTR are not used and must have their default values as values.

When Modbus function 23 is used, six new parameters are used, which are described in the table below. Each of these parameters starts with "RD\_" or "WR\_" to indicate that it belongs to the read or write task. The default is that these parameters are hidden. When using Modbus function 23, these six parameters must all be used. If you use another Modbus function, then these six parameters must have the value 0 or they must be empty. Otherwise, the STATUS value 16#818D is returned.

Table 3. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| RD\_MB\_DATA\_ADDR | IN | UInt | Start address on the remote device as of which data is to be read.  Permitted values: 0 to 65535 |
| RD\_MB\_DATA\_LEN | IN | UInt | Number of registers to be read from the remote device.  Permitted values: 1 to 125 |
| WR\_MB\_DATA\_ADDR | IN | UInt | Start address on the remote device as of which data is to be written.  Permitted values: 0 to 65535 |
| WR\_MB\_DATA\_LEN | IN | UInt | Number of registers to be written to the remote device.  Permitted values: 1 to 121 |
| RD\_MB\_DATA\_PTR | IN\_OUT | Variant | Pointer to a data buffer for the data to be read from the Modbus server.  The same data types as for MB\_DATA\_PTR are permitted as data types. |
| WR\_MB\_DATA\_PTR | IN\_OUT | Variant | Pointer to a data buffer for the data to be written to the Modbus server.  The same data types as for MB\_DATA\_PTR are permitted as data types. |

**STATUS parameter**

The meaning of the STATUS values 16#8383, 8189, 818A, 818B is expanded. The STATUS value 16#818D is added.

**Upgrade project, upgrade instruction**

When you upgrade an existing project with MB\_CLIENT instructions (e.g. instruction version V5.2), the new instruction version is not automatically used in your program. To use Modbus function 23, you must upgrade the instruction version manually.

## REQ parameter

FALSE = No Modbus communication request

TRUE = Request to communicate with a Modbus TCP server

If no instance of MB\_CLIENT is active and parameter DISCONNECT=0, when REQ=1 a new Modbus request starts. If the connection is not already established, then a new connection is made.

If the same instance of MB\_CLIENT is executed again with DISCONNECT=0 and REQ=1, before the completion of the current request, then no subsequent Modbus transmission will be made. However, as soon as the current request is completed, a new request can be processed if MB\_CLIENT is executed with REQ=1.

When the current MB\_CLIENT communication request is complete, the DONE bit is TRUE for one cycle. The DONE bit can be used as a time gate to sequence multiple MB\_CLIENT requests.

Note:

**Input data consistency during MB\_CLIENT processing**

Once a Modbus client initiates a Modbus operation, all the input states are saved internally and are then compared on each successive call. The comparison is used to determine if this particular call was the originator of the active client request. More than one MB\_CLIENT call can be performed using a common instance DB.

It is important that the inputs are not changed during the period of time that an MB\_CLIENT operation is actively being processed. If this rule is not followed, then an MB\_CLIENT cannot determine the active instance.

## MB\_MODE and MB\_DATA\_ADDR parameters select the Modbus communication function

The MB\_CLIENT instruction uses an MB\_MODE input rather than a function code. MB\_DATA\_ADDR assigns the starting Modbus address of the remote data.

The combination of MB\_MODE and MB\_DATA\_ADDR determines the function code that is used in the actual Modbus message. The following table shows the correspondence between parameter MB\_MODE, MB\_DATA\_ADDR, and Modbus function:

Table 4. Modbus functions

| **MB\_MODE** | **Modbus function** | **Data length** | **Operation and data** | **MB\_DATA\_ADDR** |
| --- | --- | --- | --- | --- |
| 0 | 01 | 1 to 2000 | Read output bits:  1 to 2000 bits per request | 1 to 9999 |
| 101 | 01 | 1 to 2000 | Read output bits:  1 to 2000 bits per request | 00000 to 65535 |
| 0 | 02 | 1 to 2000 | Read input bits:  1 to 2000 bits per request | 10001 to 19999 |
| 102 | 02 | 1 to 2000 | Read input bits:  1 to 2000 bits per request | 00000 to 65535 |
| 0 | 03 | 1 to 125 | Read Holding registers:  1 to 125 words per request | 40001 to 49999 or  400001 to 465535 |
| 103 | 03 | 1 to 125 | Read Holding registers:  1 to 125 words per request | 00000 to 65535 |
| 0 | 04 | 1 to 125 | Read input words:  1 to 125 words per request | 30001 to 39999 |
| 104 | 04 | 1 to 125 | Read input words:  1 to 125 words per request | 00000 to 65535 |
| 1 | 05 | 1 | Write one output bit:  One bit per request | 1 to 9999 |
| 105 | 05 | 1 | Write one output bit:  One bit per request | 00000 to 65535 |
| 1 | 06 | 1 | Write one holding register:  1 word per request | 40001 to 49999 or  400001 to 465535 |
| 106 | 06 | 1 | Write one holding register:  1 word per request | 00000 to 65535 |
| 1 | 15 | 2 to 1968 | Write multiple output bits:  2 to 1968 bits per request | 1 to 9999 |
| 1 | 16 | 2 to 123 | Write multiple holding registers:  2 to 123 words per request | 40001 to 49999 or  400001 to 465535 |
| 2 | 15 | 1 to 1968 | Write one or more output bits:  1 to 1968 bits per request | 1 to 9999 |
| 115 | 15 | 1 to 1968 | Write one or more output bits:  1 to 1968 bits per request | 00000 to 65535 |
| 2 | 16 | 1 to 123 | Write one or more holding registers:  1 to 123 words per request | 40001 to 49999 or  400001 to 465535 |
| 116 | 16 | 1 to 123 | Write one or more holding registers:  1 to 123 words per request | 00000 to 65535 |
| 11 | 11 | 0 | Read the server communication status word and event counter. The status word indicates busy (0 = not busy, 0xFFFF = busy). The event counter is incremented for each successful completion of a message.  Both the MB\_DATA\_ADDR and MB\_DATA\_LEN parameters of MB\_CLIENT are ignored for this function. |  |
| 80 | 08 | 1 | Check server status with diagnostic code 0x0000 (Loopback test, server echoes the request)  1 word per request |  |
| 81 | 08 | 1 | Reset server event counter with diagnostic code 0x000A  1 word per request |  |
| 123 | 23 | 1 to 121 (Write)  1 to 125 (Read) | Write holding registers of the remote device and read holding registers of the remote device in one job.  Note: This Modbus function is supported by "MB\_CLIENT" as of instruction version V6.0. The parameters RD\_MB\_DATA\_ADDR, RD\_MB\_DATA\_LEN, WR\_MB\_DATA\_ADDR, WR\_MB\_DATA\_LEN, RD\_MB\_DATA\_PTR WR\_MB\_DATA\_PTR are used for this purpose. |  |
| 3 to 10,12 to 79,82 to 100,107 to 114,117 to 255 |  |  | Reserved |  |

Note:

**MB\_DATA\_PTR assigns a buffer to store data read/written to/from a Modbus TCP server**

The data buffer can be located in a non-optimized global DB or M memory address.

For a buffer in M memory, use the Any Pointer format. This is in the format P#"Bit Address" "Data Type" "Length", an example would be P#M1000.0 WORD 500.

## MB\_DATA\_PTR parameter assigns a communication buffer

- MB\_CLIENT communication functions:

  - Read and write 1-bit data from Modbus server addresses (00001 to 09999)
  - Read 1-bit data from Modbus server addresses (10001 to 19999)
  - Read 16-bit word data from Modbus server addresses (30001 to 39999) and (40001 to 49999)
  - Write 16-bit word data to Modbus server addresses (40001 to 49999)
- Word or bit sized data is transferred to/from the DB or M memory buffer assigned by MB\_DATA\_PTR.
- If a DB is assigned as the buffer by MB\_DATA\_PTR, then you must assign data types to all DB data elements.

  - The 1-bit Bool data type represents one Modbus bit address
  - 16-bit single word data types like WORD, UInt, and Int represent one Modbus word address
  - 32-bit double word data types like DWORD, DInt, and Real represent two Modbus word addresses
- Complex DB elements can be assigned by MB\_DATA\_PTR, such as

  - Arrays
  - Named structures where each element is unique.
  - Named complex structures where each element has a unique name and a 16 or 32 bit data type.
- No requirement that the MB\_DATA\_PTR data areas be in the same global data block (or M memory area). You can assign one data block for Modbus reads, another data block for Modbus writes, or one data block for each MB\_CLIENT.

## CONNECT parameter assigns data used to establish a PROFINET connection

You must use a global data block and store the required connection data before you can reference this DB at the CONNECT parameter.

1. Create a new global DB or use an existing global DB to store the CONNECT data. You can use one DB to store multiple TCON\_IP\_v4 data structures. Each Modbus TCP client or server connection uses a TCON\_IP\_v4 data structure. You reference the connection data at the CONNECT parameter.
2. Name the DB and a static variable with a helpful name. For example, name the data block "Modbus connections" and a static variable "TCPactive\_1" (for Modbus TCP client connection 1).
3. In the DB editor, assign the system data type "TCON\_IP\_v4" in the Data Type column, for the example static variable "TCPactive\_1".
4. Expand the TCON\_IP\_v4 structure so you can modify the connection parameters, as shown in the following image.
5. Modify data in the TCON\_IP\_v4 structure for an MB\_CLIENT connection.
6. Enter the DB structure reference for the CONNECT parameter of MB\_CLIENT. For the example, this would be "Modbus connections".TCPactive\_1.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/AierzhCjxzaILmmDMOjylQ-VBkTPlmjVZAl17lebjV9hA/content?v=31a238a26deaeae9)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/AierzhCjxzaILmmDMOjylQ-VBkTPlmjVZAl17lebjV9hA)

**Modify TCON\_IP\_V4 DB data for each MB\_CLIENT connection**

- **InterfaceID**: Using the Device configuration window, click on the CPU PROFINET port image. Then click on the General properties tab and use the Hardware identifier that you see there.
- **ID**: Enter a connection ID number between 1 and 4095. Modbus TCP communication is made using underlying TCON, TDISCON, TSEND, and TRCV instructions, for OUC (Open User Communication).
- **ConnectionType**: For TCP/IP, use the default 16#0B (decimal number = 11).
- **ActiveEstablished**: This value must be 1 or TRUE. The connection is active in that MB\_CLIENT initiates Modbus communication.
- **RemoteAddress**: Enter the IP address of the target Modbus TCP server into the four ADDR array elements. For example, enter 192.168.2.241, as in the previous image.
- **RemotePort**: The default is 502. This number is the IP port number of the Modbus server that MB\_CLIENT attempts to connect and communicate with. Some third-party Modbus servers require that you use another port number.
- **LocalPort**: This value must be 0, for an MB\_CLIENT connection.

## Multiple client connections

A Modbus TCP client can support concurrent connections up to the maximum number of Open User Communications connections allowed by the PLC. The total number of connections for a PLC, including Modbus TCP Clients and Servers, must not exceed the [maximum number of supported Open User Communications connections](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/sLHuVdWZrv8gmzf1L~x4Ww?section=X0addf1af4d428dcab856741f6adb88fc).

Individual concurrent client connections must follow these rules:

- Each MB\_CLIENT connection must use a unique instance DB
- Each MB\_CLIENT connection must assign a unique server IP address
- Each MB\_CLIENT connection must assign a unique connection ID
- Unique IP port numbers may or may not be required depending upon the server configuration

A different connection ID must be used with each instance DB. In summary, the instance DB and the connection ID are paired together and must be unique for each connection.

Table 5. MB\_CLIENT instance data block: User accessible static variables

| **Variable** | **Data type** | **Default** | **description** |
| --- | --- | --- | --- |
| Blocked\_Proc\_Timeout | Real | 3.0 | Amount of time (in seconds) to wait upon a blocked Modbus client instance before removing this instance as being ACTIVE. This can occur, for example, when a client request has been issued and then application stops executing the client function before completely finishing the request. The maximum S7-1200 limit is 55 seconds. |
| MB\_Unit\_ID | Word | 255 | Modbus unit identifier:  A Modbus TCP server is addressed using its IP address. As a result, the MB\_UNIT\_ID parameter is not used for Modbus TCP addressing.  The MB\_UNIT\_ID parameter corresponds to the slave address in the Modbus RTU protocol. If a Modbus TCP server is used for a gateway to a Modbus RTU protocol, the MB\_UNIT\_ID can be used to identify the slave device connected on the serial network. The MB\_UNIT\_ID would be used to forward the request to the correct Modbus RTU slave address.  Some Modbus TCP devices may require the MB\_UNIT\_ID parameter to be within a restricted range. |
| RCV\_TIMEOUT | Real | 2.0 | Time in seconds that the MB\_CLIENT waits for a server to respond to a request. |
| Connected | Bool | 0 | Indicates whether the connection to the assigned server is connected or disconnected: 1=connected, 0=disconnected |

Table 6. MB\_CLIENT protocol errors

| **STATUS\* (W#16#)** | **Local and/or remote errors** | **Error code in the answer fromMB\_SERVER (B#16#)** | **Description** |
| --- | --- | --- | --- |
| 80C8 | Local | - | No response of the server in the defined period. Check the connection to the Modbus server. This error is only reported on completion of the configured repeated attempts.  If the "MB\_CLIENT" instruction does not receive an answer with the originally transferred transaction ID (see static tag MB\_TRANSACTION\_ID) within the defined period, this error code is output. |
| 8380 | Local | - | Received Modbus frame has incorrect format or too few bytes were received. |
| 8381 | Remote | 01 | Function code is not supported. |
| 8382 | Local | - | - The length of the Modbus frame in the frame header does not match the number of received bytes. - The number of bytes does not match the number of actually transmitted bytes (only functions 1-4). For example, this is the case when "MB\_CLIENT" requests an odd number of words, but "MB\_SERVER" always sends an even number of words. - The start address in the received frame does not match the saved start address (functions 5, 6, 15, 16). - The number of words does not match the number of actually transmitted words (functions 15 and 16). |
| Remote | 03 | Invalid length specification in received Modbus frame. Check the server side. |
| 8383 | Local | - | - Instruction version < V6.0: Error reading or writing data or access outside the address area of [MB\_DATA\_PTR](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/y4wsu061dCsHVwDY4ZbtMw?section=X67375691cebd682438c2ba87e0879acb). - Instruction version >= V6.0: Error reading or writing data or access outside the address area of MB\_DATA\_PTR, RD\_MB\_DATA\_PTR or WR\_MB\_DATA\_PTR. |
| Remote | 02 | Error reading or writing data or access outside the address area of the server |
| 8384 | Local | - | - Invalid exception code received. - A different data value was received than was originally sent by the client (functions 5, 6 and 8). - Invalid status value received (function 11) |
| Remote | 03 | Error in data value for function 5 |
| 8385 | Local | - | - Diagnostics code not supported. - A different subfunction code was received than was originally sent by the client (function 8). |
| Remote | 03 | Diagnostics code not supported |
| 8386 | Local | - | Received function code does not match the one sent originally. |
| 8387 | Local | - | The protocol ID of the Modbus TCP frame received by the server is not "0". |
| 8388 | Local | - | The Modbus server sent a different data length than was requested. This error occurs only when using the Modbus functions 5, 6, 15 or 16. |
| \* The status codes can be displayed as integer or hexadecimal values in the program editor. For information on switching the display formats, refer to "See also". | | | |

Table 7. MB\_CLIENT execution condition codes 1

| **STATUS (W#16#)** | **MB\_CLIENT parameter errors** |
| --- | --- |
| 7001 | MB\_CLIENT is waiting for a Modbus server response to a connect or disconnect request, on the assigned TCP port. This code is only returned for the first execution of a connect or disconnect operation. |
| 7002 | MB\_CLIENT is waiting for a Modbus server response to a connect or disconnect request, for the assigned TCP port. This will be returned for any subsequent executions, while waiting for completion of a connect or disconnect operation. |
| 7003 | A disconnect operation has successfully completed (Only valid for one PLC scan). |
| 80C8 | The server has not responded in the assigned time. MB\_CLIENT must receive a response using the transaction ID that was originally transmitted within the assigned time or this error is returned. Check the connection to the Modbus server device.  This error is only returned after retries (if applicable) have been attempted. |
| 8188 | The MB\_MODE parameter has an invalid value. |
| 8189 | - Instruction version < V6.0: Invalid addressing of data at the MB\_DATA\_ADDR parameter. - Instruction version >= V6.0: Invalid addressing of data at the MB\_DATA\_ADDR, RD\_MB\_DATA\_ADDR or WR\_MB\_DATA\_ADDR parameter |
| 818A | - Instruction version < V6.0: Invalid data length at the MB\_DATA\_LEN parameter. - Instruction version >= V6.0: Invalid data length at the MB\_DATA\_LEN, RD\_MB\_DATA\_LEN or WR\_MB\_DATA\_LEN parameter |
| 818B | Invalid pointer to the DATA\_PTR area. This can be the combination of MB\_DATA\_ADDRESS + MB\_DATA\_LEN. |
| 818C | Pointer DATA\_PTR points to an non-optimized DB area (must be a non-optimized DB area or M memory area) |
| 818D | One or more parameters do not have their default value but are not used with the specified Modbus function.  Example: If MB\_MODE has the value 123, MB\_DATA\_ADDR and MB\_DATA\_LEN must have the value 0 and MB\_DATA\_PTR must be empty. If MB\_MODE has a value other than 123, all parameters that begin with "RD\_" or "WR\_" must have the value 0 or be empty. |
| 8200 | The port is busy processing an existing Modbus request. |
| 8380 | Received Modbus frame is incorrect or too few bytes have been received. |
| 8387 | The assigned Connection ID parameter is different from the ID used for previous requests. There can only be a single Connection ID used within each MB\_CLIENT instance DB.  This code is also returned as an internal error if the Modbus TCP protocol ID received from a server is not 0. |
| 8388 | A Modbus server returned a quantity of data that is different than what was requested. This code applies to Modbus functions 15 or 16 only. |

1 In addition to the MB\_CLIENT errors listed above, errors can be returned from the underlying T block communication instructions (TCON, TDISCON, TSEND, and TRCV).

---

##### MB_SERVER (Communicate using PROFINET as Modbus TCP server) instruction

Table 1. MB\_SERVER instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"MB\_SERVER\_DB"(    DISCONNECT:=\_bool\_in\_,    CONNECT:=\_variant\_in\_,    NDR=>\_bool\_out\_,    DR=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    MB\_HOLD\_REG:=\_variant\_inout\_);** | MB\_SERVER communicates as a Modbus TCP server through the PROFINET port on the S7-1200 CPU. No additional communication hardware module is required.  MB\_SERVER can accept a request to connect with Modbus TCP client, receive a Modbus function request, and send a response message. |

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| DISCONNECT | IN | Bool | MB\_SERVER attempts to make a "passive" connection with a partner device. This means that the server is passively listening for a TCP connection request from any requesting IP address.  If DISCONNECT = 0 and a connection does not exist, then a passive connection can be initiated.  If DISCONNECT = 1 and a connection exists, then a disconnect operation is initiated. This parameter allows your program to control when a connection is accepted. Whenever this input is enabled, no other operation will be attempted. |
| CONNECT | IN | Variant | Reference to a Data block structure that contains connection parameters in the system data type "TCON\_IP\_v4". The following data types are also supported: TCON\_IP\_V4, TCON\_QDN and TCON\_QDN\_SEC. See ["Parameters for the PROFINET connection"](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/4KPJfLxRtqynTXLM0pgSaQ?section=X868ef9f6da288ebcc92dd27a15c9077b). |
| MB\_HOLD\_REG | IN\_OUT | Variant | Pointer to the MB\_SERVER Modbus holding register: The holding register must either be a non-optimized global DB or an M memory address. This memory area is used to hold the data a Modbus client is allowed to access using Modbus register functions 3 (read), 6 (write), 16 (write), and 23 (write/read). |
| NDR | OUT | Bool | New Data Ready: 0 = No new data, 1 = Indicates that new data has been written by a Modbus client |
| DR | OUT | Bool | Data Read: 0 = No data read, 1 = Indicates that data has been read by a Modbus client. |
| ERROR | OUT | Bool | The ERROR bit is TRUE for one scan, after MB\_SERVER execution ended with an error. The error code at the STATUS parameter is valid only during the single cycle where ERROR = TRUE. |
| STATUS | OUT | Word | Execution condition code |

## CONNECT parameter assigns data used to establish a PROFINET connection

You must use a global data block and store the required connection data before you can reference this DB at the CONNECT parameter.

1. Create a new global DB or use an existing global DB to store the CONNECT data. You can use one DB to store multiple TCON\_IP\_v4 data structures. Each Modbus TCP client or server connection uses a TCON\_IP\_v4 data structure. You reference the connection data at the CONNECT parameter.
2. Name the DB and a static variable with a helpful name. For example, name the data block "Modbus connections" and a static variable "TCPpassive\_1" (for Modbus TCP server connection 1).
3. In the DB editor, assign the system data type "TCON\_IP\_v4" in the Data Type column, for the example static variable "TCPactive\_1".
4. Expand the TCON\_IP\_v4 structure so you can modify the connection parameters, as shown in the following image.
5. Modify data in the TCON\_IP\_v4 structure for an MB\_SERVER connection.
6. Enter the DB structure reference for the CONNECT parameter of MB\_SEVER. For the example, this would be "Modbus connections".TCPpassive\_1.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/6H6kdo35I0AbykfOFeq25w-VBkTPlmjVZAl17lebjV9hA/content?v=3da084cacb4f6f9b)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/6H6kdo35I0AbykfOFeq25w-VBkTPlmjVZAl17lebjV9hA)

**Modify TCON\_IP\_V4 DB data for each MB\_SERVER connection**

- **InterfaceID**: Using the Device configuration window, click on the CPU PROFINET port image. Then click on the General properties tab and use the Hardware identifier that you see there.
- **ID**: Enter a number between 1 and 4095 that is unique for this connection. Modbus TCP communication is made using underlying TCON, TDISCON, TSEND, and TRCV instructions, for OUC (Open User Communication). Up to eight simultaneous OUC connections are allowed.
- **ConnectionType**: For TCP/IP, use the default 16#0B (decimal value = 11).
- **ActiveEstablished**: This value must be 0 or FALSE. The connection is passive in that MB\_SERVER is waiting for a communication request from a Modbus client.
- **RemoteAddress**: There are two options.

  - Use 0.0.0.0 and MB\_CLIENT will respond to a Modbus request from any TCP client
  - Enter the IP address of a target Modbus TCP client and MB\_CLIENT only responds to a request originating from this client's IP address. For example, enter 192.168.2.241, as in the previous image.
- **RemotePort**: This value must be 0, for an MB\_SERVER connection.
- **LocalPort**: The default is 502. This number is the IP port number of the Modbus client that MB\_SERVER attempts to connect and communicate with. Some third-party Modbus clients require another port number.

## Modbus and process image addresses

MB\_SERVER allows incoming Modbus function codes (1, 2, 4, 5, and 15) to read/write bits/words directly in the input/output process image. For data transfer function codes (3, 6, and 16), the MB\_HOLD\_REG parameter must be defined as a data type larger than a byte. The following table shows the mapping of Modbus addresses to the process image in the CPU.

Table 3. Mapping of Modbus addresses to the process image

| **Modbus functions** | | | | | | **S7-1200** | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Codes | Function | Data area | Address range | | | Data area | CPU address |
| 01 | Read bits | Output | 1 | To | 8192 | Output Process Image | Q0.0 to Q1023.7 |
| 02 | Read bits | Input | 10001 | To | 18192 | Input Process Image | I0.0 to I1023.7 |
| 04 | Read words | Input | 30001 | To | 30512 | Input Process Image | IW0 to IW1022 |
| 05 | Write bit | Output | 1 | To | 8192 | Output Process Image | Q0.0 to Q1023.7 |
| 15 | Write bits | Output | 1 | To | 8192 | Output Process Image | Q0.0 to Q1023.7 |

Incoming Modbus message function codes function codes (3, 6, and 16) read/write words in a Modbus holding register, which can be in M memory or a data block. The type of holding register is specified by the MB\_HOLD\_REG parameter.

Note:

**MB\_HOLD\_REG parameter assignment**

Modbus holding registers defined as arrays of word, integer, wide character, unsigned integer, byte, short integer, unsigned short integer, character, double word, double integer, unsigned double integer, or real can be placed in any memory area.

You must place Modbus holding registers that you defined as structures in non-optimized DBs.

For a Modbus holding register in M memory, use the Any Pointer format. This is in the format P#"Bit Address" "Data Type" "Length". An example would be P#M1000.0 WORD 500.

The following table shows examples of Modbus addresses to holding register mapping used for Modbus function codes 03 (read words), 06 (write word), and 16 (write words). The actual upper limit of DB addresses is determined by the maximum work memory limit and M memory limit, for each CPU model.

Warning:

**Risks with access to the process image**

Each Modbus TCP client has read and write access to the process image inputs and outputs, and to the data block or bit memory area defined by the Modbus holding register. Unauthorized read and write operations can change PLC variables into invalid values and disrupt process operations.

To reduce the risk of unauthorized access, restrict access to an IP address of a specific Modbus client. For information on additional industrial security measures that can be implemented, please visit the [Siemens Industrial Cybersecurity Web site](https://www.siemens.com/global/en/products/automation/topic-areas/industrial-cybersecurity.html).

Disruption of process operations can result in death, severe injury and/or property damage.

Table 4. Mapping examples of Modbus address to CPU memory address

| **Modbus Address** | **MB\_HOLD\_REG parameter examples** | | |
| --- | --- | --- | --- |
| **P#M100.0 Word 5** | **P#DB10.DBx0.0 Word 5** | **"Recipe".ingredient** |
| 40001 | MW100 | DB10.DBW0 | "Recipe".ingredient[1] |
| 40002 | MW102 | DB10.DBW2 | "Recipe".ingredient[2] |
| 40003 | MW104 | DB10.DBW4 | "Recipe".ingredient[3] |
| 40004 | MW106 | DB10.DBW6 | "Recipe".ingredient[4] |
| 40005 | MW108 | DB10.DBW8 | "Recipe".ingredient[5] |

## Modbus Application Protocol header

The Modbus Application Protocol header is the first seven bytes of every Modbus TCP message. This header contains the Transaction Identifier, Protocol Identifier, Length, and Unit Identifier. The MB\_SERVER instruction response message contains the same values for the Transaction Identifier, Protocol Identifier, and Unit Identifier that were received in the Modbus request message. The Length field is calculated by the MB\_SERVER instruction.

## Multiple server connections

Multiple server connections may be created. A single PLC can establish concurrent connections to multiple Modbus TCP clients.

A Modbus TCP server can support concurrent connections up to the maximum number of Open User Communications connections allowed by the PLC. The total number of connections for a PLC, including Modbus TCP Clients and Servers, must not exceed the [maximum number of supported Open User Communications connections](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/sLHuVdWZrv8gmzf1L~x4Ww?section=X0addf1af4d428dcab856741f6adb88fc). The Modbus TCP connections may be shared between Client and Server type connections.

Individual concurrent server connection must follow these rules:

- Each MB\_SERVER connection must use a unique instance DB.
- Each MB\_SERVER connection must assign a unique IP port number. Only 1 connection per port is supported.
- Each MB\_SERVER connection must assign a unique connection ID.
- The MB\_SERVER must be called individually for each connection (with its respective instance DB).

The connection ID must be unique for each individual connection. A single, connection ID must be used with each individual instance DB. The instance DB and the connection ID are paired together and must be unique for every connection.

Table 5. Modbus diagnostic function codes

| **MB\_SERVER Modbus diagnostic functions** | | |
| --- | --- | --- |
| Codes | Sub-function | Description |
| 08 | 0x0000 | Return query data echo test: The MB\_SERVER will echo back to a Modbus client a data word that is received. |
| 08 | 0x000A | Clear communication event counter: The MB\_SEVER will clear the communication event counter that is used for Modbus function 11. |
| 11 |  | Get communication event counter: The MB\_SERVER uses an internal communication event counter for recording the number of successful Modbus read and write requests that are sent to the Modbus server. The counter does not increment on any request for Function 8, Function 11, or any request that results in a communication error.  The broadcast function is not available for Modbus TCP, because only one client-server connection exists at any one time. |

## MB\_SERVER instruction data block (DB) variables

This table shows the public static variables that are stored in the MB\_SERVER instance data block and can be used in your program

Table 6. MB\_SERVER public static variables

| **Variable** | **Data type** | **Default** | **Description** |
| --- | --- | --- | --- |
| HR\_Start\_Offset | Word | 0 | Assigns the starting address of the Modbus Holding register |
| Request\_Count | Word | 0 | The number of all requests received by this server. |
| Server\_Message\_Count | Word | 0 | The number of requests received for this specific server. |
| Xmt\_Rcv\_Count | Word | 0 | The number of transmissions or receptions that have encountered an error. Also, incremented if a message is received that is an invalid Modbus message. |
| Exception\_Count | Word | 0 | Modbus specific errors that require a returned exception |
| Success\_Count | Word | 0 | The number of requests received for this specific server that has no protocol errors. |
| Connected | Bool | 0 | Indicates whether the connection to the assigned client is connected or disconnected: 1=connected, 0=disconnected |
| QB\_Start | UInt | 0 | The starting address of the output bytes to which the CPU can write (QB0 to QB65535) |
| QB\_Count | UInt | 65535 | The number of bytes to which a remote device can write. If QB\_Count = 0, a remote device cannot write to the outputs.  Example: To allow only QB10 through QB17 to be writable, QB\_Start = 10 and QB\_Count = 8. |
| QB\_Read\_Start | UInt | 0 | The starting address of the output bytes to which the CPU can read (QB0 to QB65535) |
| QB\_Read\_Count | UInt | 65535 | The number of output bytes from which a remote device can read. If QB\_Count = 0, a remote device cannot read from the outputs. Example: To allow only QB10 through QB17 to be readable, QB\_Start = 10 and QB\_Count = 8. |
| IB\_Read\_Start | UInt | 0 | The starting address of the input bytes to which the CPU can read (IB0 to IB65535) |
| IB\_Read\_Count | UInt | 65535 | The number of input bytes from which a remote device can read. If IB\_Count = 0, a remote device cannot read from the inputs. Example: To allow only IB10 through IB17 to be readable, IB\_Start = 10 and IB\_Count = 8. |
| NDR\_immediate | Bool | FALSE | Identical meaning as the parameter NDR (New Data Ready). The MB\_SERVER updates the "NDR\_immediate" in the same call that processes a Modbus TCP write request. |
| DR\_immediate | Bool | FALSE | Identical meaning as the parameter DR (Data Read). The MB\_SERVER updates the "DR\_immediate" in the same call that processes a Modbus TCP write request. |

Your program can write data to the control Modbus server operations and the following variables:

- HR\_Start\_Offset
- QB\_Start
- QB\_Count
- QB\_Read\_Start
- QB\_Read\_Count
- IB\_Read\_Start
- IB\_Read\_Count

Version requirements for MB\_SERVER instruction data block (DB) variables availability are as follows:

Table 7. MB\_SERVER instruction data block (DB) variables availability version requirements: Instruction, TIA Portal, and S7‑1200 CPU

| **MB\_SERVER instruction version** | **TIA Portal version** | **S7-1200 CPU firmware (FW) version** | **Data block variables** |
| --- | --- | --- | --- |
| 4.2 | V14 SP1 | CPU FW V4.0 or later | QB\_Start |
| QB\_Count |
| 5.0 or later | V15 or later | CPU FW V4.2 or later | QB\_Start |
| QB\_Count |
| QB\_Read\_Start |
| QB\_Read\_Count |
| IB\_Read\_Start |
| IB\_Read\_Count |
| NDR\_immediate |
| DR\_immediate |

## HR\_Start\_Offset

Modbus holding register addresses begin at 40001. These addresses correspond to the beginning PLC memory address of the holding register. However, you can use the "HR\_Start\_Offset" variable to start the beginning Modbus holding register address at another number instead of 40001.

For example, if the holding register starts at MW100 and is 100 words long. An offset of 20 specifies a beginning holding register address of 40021 instead of 40001. Any address less than 40021 or greater than 40119 results in an addressing error.

Table 8. Example of Modbus holding register addressing

| **HR\_Start\_Offset** | **Address** | **Minimum** | **Maximum** |
| --- | --- | --- | --- |
| 0 | Modbus address (Word) | 40001 | 40099 |
| S7-1200 address | MW100 | MW298 |
| 20 | Modbus address (Word) | 40021 | 40119 |
| S7-1200 address | MW100 | MW298 |

HR\_Start\_Offset is word data in the MB\_SERVER instance data block that assigns the starting address of the Modbus holding register. You can set this public static variable by using the parameter helper drop list, after MB\_SERVER is placed in your program.

For example, after you place MB\_SERVER in a LAD network, you can go to a previous network and assign HR\_Start\_Offset. The start address must be assigned prior to execution of MB\_SERVER.

|  |  |
| --- | --- |
|  | Entering a Modbus server  variable using the default DB name:   1. Set the cursor in the parameter field and type an m character. 2. Select "MB\_SERVER\_DB" from the drop list of DB names. 3. Select "MB\_SERVER\_DB.HR\_Start\_Offset" from the drop list of DB variables. |
|  |
|  |

## Access to data areas in data blocks (DB) instead of direct access to Modbus addresses

You can access data areas in DBs. In the global DB "Attributes" Property page, you must deselect the "Only store in load memory" and "Optimized block access" check boxes.

If a Modbus request arrives and you did not define a data area for the Modbus data type of the corresponding function code, the MB\_SERVER instruction treats the request as in previous instruction versions: You access process images and holding registers directly.

If you have defined a data area for the Modbus data type of the function code, the MB\_SERVER instruction reads from or writes to that data area. Whether it reads or writes depends on the job type.

Note:

If a data area is configured, the MB\_SERVER instruction ignores the offsets or ranges configured by the static variables in the instance data block that corresponds to the data\_type of the data area. Those offsets and ranges only apply to the process image or the memory referenced by MB\_HOLD\_REG. The data area start and length parameters provide its own way of defining offsets and ranges

For one individual Modbus request, you can only read from or write to one data area. If, for example, you want to read holding registers that extend over multiple data areas, you require multiple Modbus requests.

These are the rules for defining data areas:

- You can define up to eight data areas in different DBs; each DB must only contain one data area. An individual MODBUS request can only read from precisely one data area or write to precisely one data area. Each data area corresponds to one MODBUS address area. You define the data areas in the "Data\_Area\_Array" static tag of the instance DB.
- If you want to use less than eight data areas, you must place the required data areas one behind the other, without any gaps. The first blank entry in the data areas ends the data area search during processing. If, for example, you define the field elements 1, 2, 4, and 5, the "Data\_Area\_Array" only recognizes field elements 1 and 2. as field element 3 is empty.
- The Data\_Area\_Array field consists of eight elements: Data\_Area\_Array[1] to Data\_Area\_Array[8]
- Each field element Data\_Area\_Array[x], 1 <= x <= 8, is a UDT of the type MB\_DataArea and is structured as follows:

  | **Parameter** | **Data type** | **Meaning** |
  | --- | --- | --- |
  | data\_ type | UInt | Identifier for the MODBUS data type that is mapped to this data area:  - 0: Identifier for an empty field element or an unused data area. In this case, the values of db, start and length are irrelevant. - 1: Process image output (used with function codes 1, 5, and 15) - 2: Process image input (used with function code 2) - 3: Holding register (used with function codes 3, 6, and 16) - 4: Input register (used with function code 4) Note: If you have defined a data area for a MODBUS data type, the instruction MB\_SERVER can no longer access this MODBUS data type directly. If the address of a MODBUS request for such a data type does not correspond to a defined data area, a value of W#16#8383 is returned in STATUS. |
  | db | UInt | Number of the data block to which the MODBUS register or bits subsequently defined are mapped  The DB number must be unique in the data areas. The same DB number must not be defined in multiple data areas.  In the global DB "Attributes" Property page, you must deselect the "Only store in load memory" and "Optimized block access" check boxes.  Data areas also start with the byte address 0 of the DB.  Permitted values: 1 to 60999 |
  | start | UInt | First MODBUS address that is mapped to the data block starting from address 0.0  Permitted values: 0 to 65535 |
  | length | UInt | Number of bits (for the values 1 and 2 of data\_type) or number of registers (for the values 3 and 4 of data\_type)  The MODBUS address areas of one and the same MODBUS data type must not overlap.  Permitted values: 1 to 65535 |

Examples of the definition of data areas:

- First example: data\_type = 3, db = 1, start = 10, length = 6

  The CPU maps the holding registers (data\_type = 3) in data block 1 (db = 1), placing the Modbus address 10 (start = 10) at data word 0 and the last valid Modbus address 15 (length = 6) at data word 5.
- Second example: data\_type = 2, db = 15, start = 1700, length = 112

  The CPU maps the inputs (data\_type = 2) in data block 15 (db = 15), placing the Modbus address 1700 (start = 1700) at data word 0 and the last valid Modbus address 1811 (length = 112) at data word 111.

## Condition codes

Table 9. MB\_SERVER execution condition codes 1

| **STATUS (W#16#)** | **Response code to Modbus server (B#16#)** | **Modbus protocol errors** |
| --- | --- | --- |
| 7001 |  | MB\_SERVER is waiting for a Modbus client to connect to the assigned TCP port. This code is returned on the first execution of a connect or disconnect operation. |
| 7002 |  | MB\_SERVER is waiting for a Modbus client to connect to the assigned TCP port. This code is returned for any subsequent executions, while waiting for completion of a connect or disconnect operation. |
| 7003 |  | A disconnect operation has successfully completed (Only valid for one PLC scan). |
| 8187 |  | MB\_HOLD\_REG is not valid, could be pointing into an optimized DB, or is pointing to an area of less than 2 bytes. |
| 818C |  | Pointer MB\_HOLD\_REG points to a non-optimized DB area (must be a non-optimized global DB area or M memory area) or Blocked process timeout exceeds the limit of 55 seconds. (S7-1200 specific) |
| 8381 | 01 | Function code not supported |
| 8382 | 03 | Error in data length:   - Invalid length specification in received Modbus frame. - The frame length entered in the header of the Modbus frame does not match the number of actually received bytes. - The number of bytes entered in the header of the Modbus frame does not match the number of actually received bytes (functions 15 and 16). |
| 8383 | 02 | Data address error or access outside the bounds of the MB\_HOLD\_REG address area |
| 8384 | 03 | Data value error |
| 8385 | 03 | Data diagnostic code not supported (function code 08) |
| 8389 |  | Invalid data area definition:   - Invalid data\_type value - DB number invalid or does not exist:    - Invalid db value   - DB number does not exist   - DB number is already used by another data area   - DB with optimized access   - DB is not located in the work memory  - Invalid length value  - Overlapping of MODBUS address ranges that belong to the same MODBUS data type |

1 In addition to the MB\_SERVER errors listed above, errors can be returned from the underlying T block communication instructions (TCON, TDISCON, TSEND, and TRCV).

---

##### MB_RED_CLIENT (Redundant communication over PROFINET as a Modbus TCP client)

You can use this instruction to establish a connection between an S7-1200 CPU and a device that supports the Modbus TCP protocol.

Table 1. MB\_RED\_CLIENT instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"MB\_RED\_CLIENT\_DB"(    REG\_KEY:=\_string\_in\_,    USE\_ALL\_CONN:=\_bool\_in\_    REQ:=\_bool\_in\_,    DISCONNECT:=\_bool\_in\_,    MB\_MODE:=\_usint\_in\_,    MB\_DATA\_ADDR:=\_udint\_in\_,    MB\_DATA\_LEN:=\_uint\_in\_,    LICENSED=>\_bool\_out\_    IDENT\_CODE=>\_string\_out\_    DONE=>\_bool\_out\_,    BUSY=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS\_0A=>\_word\_out\_,    STATUS\_1A=>\_word\_out\_,    STATUS\_0B=>\_word\_out\_,    STATUS\_1B=>\_word\_out\_,    RED\_ERR\_S7=>\_bool\_out\_,    RED\_ERR\_DEV=>\_bool\_out\_,    TOT\_COM\_ERR=>\_bool\_out\_,    MB\_DATA\_PTR:=\_variant\_inout\_);** | The MB\_RED\_CLIENT instruction communicates as a Modbus TCP client over the PROFINET connection.  You use the instruction MB\_RED\_CLIENT to establish a redundant connection between the client and the server, send Modbus requests, receive responses, and control connection termination by the Modbus TCP client. |

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REG\_KEY 1 | IN | STRING[17] | Registration code for licensing  The MB\_RED\_CLIENT instruction must be licensed on each CPU individually. |
| USE\_ALL\_CONN | IN | Bool | Specify the number of configured connections over which the frame is to be sent:   - 0: Send frame over one connection, switch to next connection only in case of error - 1: Send frame over all configured connections |
| REQ | IN | Bool | Modbus query to the Modbus TCP server  The REQ parameter is level-controlled. This means that as long as the input is set (REQ = TRUE), the instruction sends communication requests. If the connection has not been established yet, it is established now, and the Modbus frame is sent immediately thereafter.  Changes to the input parameters will not become effective until the server has responded, or an error message has been output.  If the parameter REQ is set again during an ongoing Modbus request, no additional transmission takes place afterwards. |
| DISCONNECT | IN | Bool | With this parameter, you control the establishment and termination of the connection to the Modbus server:   - 0: Establish communication connection to the connection partner configured at the CONNECT parameter (see CONNECT parameter). - 1: Disconnect the communication connection. No other function is executed during connection termination. The value 0003 is output at the STATUS\_x parameter after successful connection termination. |
| MB\_MODE 2 | IN | USInt | Selects the mode of the Modbus request (read, write or diagnostics) or direct selection of a Modbus function |
| MB\_DATA\_ADDR 2 | IN | UDInt | Modbus address depending on MB\_MODE |
| MB\_DATA\_LEN | IN | UInt | Data length: Number of bits or registers for the data access |
| MB\_DATA\_PTR 2 | IN\_OUT | Variant | Pointer to a data buffer for the data to be received from the Modbus server or to be sent to the Modbus server. |
| LICENSED 1 | OUT | Bool | - 0: Instruction is not licensed - 1: Instruction is licensed |
| IDENT\_CODE 1 | OUT | STRING[18] | Identification for licensing. Use this string to request the REG\_KEY registration code. |
| DONE | OUT | Bool | The bit at the DONE output parameter is set to "1" as soon as the activated Modbus job is completed without errors on at least one connection. |
| BUSY | OUT | Bool | - 0: No Modbus request in progress - 1: Modbus request being processed   The BUSY output parameter is not set during connection establishment and termination. |
| ERROR | OUT | Bool | - 0: No error - 1: The activated Modbus job could not be transmitted successfully on any of the configured connections. The cause of error is indicated by the STATUS\_x parameter. |
| STATUS\_0A 3 | OUT | Word | Detailed status information of the instruction on connection 0A. |
| STATUS\_1A 3 | OUT | Word | Detailed status information of the instruction on connection 1A. |
| STATUS\_0B 3 | OUT | Word | Detailed status information of the instruction on connection 0B. |
| STATUS\_1B 3 | OUT | Word | Detailed status information of the instruction on connection 1B. |
| RED\_ERR\_S7 3 | OUT | Bool | - 0: No redundancy error in SIMATIC - 1: Redundancy error in SIMATIC |
| RED\_ERR\_S7 3 | OUT | Bool | - 0: No redundancy error on side of link partner - 1: Redundancy error on side of link partner |
| RED\_ERR\_S7 3 | OUT | Bool | - 0: At least 1 configured connection is established - 1: Complete loss of communication, all configured connections are terminated |

1 Refer to the "Licensing" section below for further information.

2 Refer to the "Input parameters: MB\_MODE, MB\_DATA\_ADDR, MB\_DATA\_LEN, and MB\_DATA\_PTR" section below for further information.

3 Refer to the "Output parameters: STATUS\_x, RED\_ERR\_S7, RED\_ERR\_DEV, and TOT\_COM\_ERR" section below for further information.

Note:

**Consistent input data during an MB\_RED\_CLIENT call**

When a Modbus client instruction is called, the values of the input parameters are stored internally. The values must not be changed while the frame is being processed.

## Multiple client connections

The CPUs can process multiple Modbus TCP client connections. The maximum number of connections depends on the CPU being used and can be found in the technical specifications of the CPU. The total number of connections of one CPU, including those of the Modbus TCP clients and server must not exceed the maximum number of supported connections.

With individual client connections, remember the following rules:

- Each MB\_RED\_CLIENT connection must use a unique instance DB.
- For each MB\_RED\_CLIENT connection, a unique server IP address must be specified.
- Each MB\_RED\_CLIENT connection requires a unique connection ID. The connection IDs must be unique throughout the CPU.

## Operation and redundancy

The communication nodes can be designed as standalone or redundant. If one of the partners is designed as standalone, we refer to it as single-sided redundancy. If both partners are designed redundantly, we refer to it as double-sided redundancy:

- Single-sided redundancy:

  - Description: One connection each must be configured for each connection between the communication partners. The connection points of the **SIMATIC S7** are referred to as **0** and **1**; the connection points of the **communication partner** are referred to as **A** and **B**. The R-CPU or H-CPU 1 refers to the connection point 0, the R-CPU or H-CPU 2 refers to the connection point 1.
  - Configuration: If the S7 is designed redundantly, one connection is created from the S7 connection point 0 to junction A of the link partner (Connection from the S7 connection point **0** to the partner/node **A** => connection **0A**), and one connection from the S7 connection point 1 to junction A of the link partner (Connection from the S7 connection point **1** to the partner/node **A** => connection **1A**). The figure illustrates the connection designations:

    Figure 1. Single-sided redundancy S7[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/YFxUioGjR_CKtPDfRi4cpg-VBkTPlmjVZAl17lebjV9hA/content?v=d6bbb42c55865cc1)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/YFxUioGjR_CKtPDfRi4cpg-VBkTPlmjVZAl17lebjV9hA)
  - If the S7 is designed as standalone and the link partner is designed redundantly, one connection is created from the S7 connection point 0 to junction A of the link partner (connection from the S7 connection point **0** to the partner/node **A** => connection **0A**), and one connection from the S7 connection point 0 to junction B of the link partner (connection from the S7 connection point **0** to the partner/node **B** => connection **0B**). The figure illustrates the connection designations:

    Figure 2. Single-sided redundancy partner[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/z6xvjZ1xJOBS7W8E_xZqUw-VBkTPlmjVZAl17lebjV9hA/content?v=880f903dc24f2a46)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/z6xvjZ1xJOBS7W8E_xZqUw-VBkTPlmjVZAl17lebjV9hA)
- Double-sided redundancy:

  - Description: One connection each must be configured for each connection between the communication partners. The connection points of the SIMATIC S7 are referred to as **0** and **1**; the connection points of the **communication partner** are referred to as **A** and **B**.

    The R-CPU or H-CPU 1 refers to the connection point 0 the R-CPU or H-CPU 2 refers to the connection point 1.
  - Configuration: In the case of double-sided redundancy, two connections are created from connection point 0 (connection from the S7 connection point **0** to the partner/node **A** => connection **0A** and connection from the S7 connection point **0** to the partner/node **B** => connection **0B**), and two connections from connection point 1 of the S7 to the junctions A and B of the link partner (connection from the S7 connection point **1** to the partner/node **A** => connection **1A** and connection from the S7 connection point **1** to the partner/node **B** => connection **1B**). The figure illustrates the connection designations:

    Figure 3. Double-sided redundancy[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/uDUvJ9Cv2SmQqeHbJTtcKA-VBkTPlmjVZAl17lebjV9hA/content?v=fce3149035ccfe48)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/uDUvJ9Cv2SmQqeHbJTtcKA-VBkTPlmjVZAl17lebjV9hA)
- Frame processing: The frames can be sent via one or via all configured connections:

  - Send frames via one connection: The MODBUS frame is sent via one - the currently active - connection with the setting USE\_ALL\_CONN = FALSE. In case of a timeout (no response from the server) or a connection fault an attempt is made to send the frame via the other (maximum 4) configured connections. The sequence is then 0A, 1A, 0B and 1B. If a frame was transmitted successfully via a connection, this connection is marked as "active" and the further frame traffic is executed via this connection. In the case of a connection fault of the active connection it is again attempted to send the frame via all configured connections. If all send attempts fail, ERROR and STATUS\_x are set accordingly.

    If a response frame was received, a plausibility check is executed. If this check is successful, the required actions are performed and the job is executed without errors; the output DONE is set. If errors are detected during the check, the job is ended without errors, the bit ERROR is set and an error number is displayed at STATUS\_x. In this case no new attempt is made to send the frame on the next configured connection. A switchover to the other configured connections only takes place if a connection fault was detected or no response was received.
  - Sending frames via all connections: The MODBUS frame is sent via all configured, established connections with the setting USE\_ALL\_CONN = TRUE. A validity check is performed after the response frame has been received on one of the connections. If this check is successful, the required actions are performed. If a valid response frame was received on at least one connection, the output DONE is set.
- Redundancy outputs RED\_ERR\_S7, RED\_ERR\_DEV, and TOT\_COM\_ERR:

  - The redundancy bits RED\_ERR\_S7, RED\_ERR\_DEV, and TOT\_COM\_ERR are set based on the states of the status outputs:

    Figure 4. Display of the interrupt bits for redundancy setup on both sides[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/bWD67_LXVkIXYY0rDDTv0A-VBkTPlmjVZAl17lebjV9hA/content?v=42bff8eb824525d9)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/bWD67_LXVkIXYY0rDDTv0A-VBkTPlmjVZAl17lebjV9hA)

    Figure 5. Display of the interrupt bits for redundancy setup on one side[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/VBLO6ke8AddG5fXgwrxipg-VBkTPlmjVZAl17lebjV9hA/content?v=d5233145ed3f00d0)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/VBLO6ke8AddG5fXgwrxipg-VBkTPlmjVZAl17lebjV9hA)

Note:

**Port numbers for client and server**

The Modbus client uses a port number starting at 2000. The Modbus server is usually addressed over the port number 502.

## Parameter assignment

You can use the MB\_RED\_CLIENT instruction **V1.0** and **V1.1** for S7-1200. The CPU implements the connections over the local interface of the CPU or CM/CP. The CPU configures and establishes the connections using the TCON\_IP\_V4 structure.

Configuration of MB\_RED\_CLIENT: You make the following settings using the configuration dialog of the MB\_RED\_CLIENT instruction:

- Connection parameters for the connections 0A, 1A, 0B and 1B (Refer to "Operation and Redundancy", above, for more information on redundancy configuration.)
- Internal parameter (optional)

You can open the configuration dialog with the MB\_RED\_CLIENT instruction or through the technology objects:

Figure 6. Parameterized client connection[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/_4c0KB87~b1h6pbPBA3KTA-VBkTPlmjVZAl17lebjV9hA/content?v=6f82a7f32f85f5c9)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/_4c0KB87~b1h6pbPBA3KTA-VBkTPlmjVZAl17lebjV9hA)

Figure 7. Configured client connection[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/INBMkAeEAm9uv2ibHzgOZg-VBkTPlmjVZAl17lebjV9hA)

| **Tag** | **Start value** | **Description** |
| --- | --- | --- |
| **Configured connections** | | |
| Interface ID | 64 | HW identifier of the PN interface used |
| Connection ID | 16#0000 | Connection IDs for the connections used  These connection IDs must be unique throughout the CPU. |
| Local port | 0 | Local port number of the client. By default, no port number is entered for the client. |
| Remote IP | 0.0.0.0 | Remote IP address of the server |
| Remote port | 502 | Remote port number of the server  The default port for Modbus/TCP server is 502. |
| **Configured connections** | | |
| Interface ID | 64 | HW identifier of the PN interface used |
| Connection ID | 16#0000 | Connection IDs for the connections used  These connections are configured in the network view. |

Figure 8. Internal parameter (optional)[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/HJt_WlJi0KpJROQESaSzHQ-VBkTPlmjVZAl17lebjV9hA/content?v=2eb9b8098a080c7a)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/HJt_WlJi0KpJROQESaSzHQ-VBkTPlmjVZAl17lebjV9hA)

| **Tag** | **Data type** | **Start value** | **Description** |
| --- | --- | --- | --- |
| Blocked Proc Time | REAL | 3.0 | Wait time in seconds before the static tag ACTIVE is reset if there is a blocked Modbus instance. This can, for example, occur if a client request is output and the execution of the client function aborts before the request was fully executed. The wait time must be between 0.5 s and 55 s. |
| Receive timeout | REAL | 2.0 | Time interval in seconds in which the "MB\_RED\_CLIENT" instruction waits for a response from the server. It must be between 0.5 s and 55 s. |
| MB\_Unit\_ID | BYTE | 255 | Modbus device detection:  A Modbus TCP server is addressed using its IP address. For this reason, the MB\_UNIT\_ID parameter is not used in the case of Modbus TCP addressing.  The MB\_UNIT\_ID parameter corresponds to the field of the slave address in the Modbus RTU protocol. If a Modbus/TCP server is used as a gateway for a Modbus RTU protocol, the slave device in the serial network can be identified using MB\_UNIT\_ID. The MB\_UNIT\_ID parameter would in this case forward the request to the correct Modbus RTU slave address.  Please note that some Modbus/TCP devices may require the MB\_UNIT\_ID parameter for the initialization within a limited value range. |
| Retries | WORD | 3 | Number of send attempts made by the MB\_RED\_CLIENT instruction before it returns the error W#16#80C8. |

Note:

**Tag MB\_Transaction\_ID**

If the transaction ID in the answer of the Modbus TCP server does not match the transaction ID of the job from MB\_RED\_CLIENT, the MB\_RED\_CLIENT instruction waits for the time period RCV\_TIMEOUT \* RETRIES for the answer of the Modbus TCP server with the correct transaction ID; once this time has expired, it returns the error W#16#80C8.

## Licensing

The MB\_RED\_CLIENT instruction is subject to a fee, and you must license the instruction on each CPU individually. Licensing takes place in two steps:

- Displaying the license IDENT\_CODE
- Entering the REG\_KEY registration key: You must assign the REG\_KEY registration key at each MB\_RED\_CLIENT instruction. Save the REG\_KEY in a global data block from which all MB\_RED\_CLIENT instructions receive the necessary registration key.

Procedure for displaying the license IDENT\_CODE:

1. Assign parameters to the MB\_RED\_CLIENT instruction in line with your requirements in a cyclic OB. Download the program to the CPU and set the CPU to RUN.
2. Open the instance DB of the Modbus instruction, and click the "Monitor all" button.
3. The instance DB displays an 18-digit character string at the IDENT\_CODE output.

   Figure 9. License[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/0qaxC9yCwDBYgNl0vvLaew-VBkTPlmjVZAl17lebjV9hA/content?v=bc5395163158b154)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/0qaxC9yCwDBYgNl0vvLaew-VBkTPlmjVZAl17lebjV9hA)
4. Copy this string using copy/paste from the data block and paste it in the form (that was sent to you by email after you ordered the product or is included on the CD).
5. Send the form to [Customer support](https://support.industry.siemens.com/my/ww/en/requests/) using a service request. You will then receive the registration key for your CPU.

Procedure for entering the registration key REG\_KEY:

1. Insert a new global data block with a unique symbolic name, for example "License\_DB", using "Add new block…".
2. Create a REG\_KEY parameter in this block with the data type STRING[17].

   Figure 10. REG KEY[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/T85Qf2eNVUgW_Qi1nvru7w-VBkTPlmjVZAl17lebjV9hA/content?v=8c6ba9deed873cd9)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/T85Qf2eNVUgW_Qi1nvru7w-VBkTPlmjVZAl17lebjV9hA)
3. Copy the transmitted 17-digit registration key using copy/paste to the "Start value" column.
4. In the cyclic OB, enter the name of the license DB and the name of the string (for example, License\_DB.REG\_KEY) at the REG\_KEY parameter of the MB\_RED\_CLIENT instruction.
5. Download the modified blocks to the CPU. You can enter the registration key during runtime; a change from STOP to RUN is not necessary.
6. The Modbus/TCP communication using the MB\_RED\_CLIENT instruction is now licensed for this CPU; the LICENSED output bit is TRUE.

Procedure for correcting missing or incorrect licensing:

- If you enter an incorrect registration key or no registration key, the ERROR LED of the CPU flashes. In addition, for the S7-1200, the CPU makes a cyclic entry in the diagnostics buffer regarding the missing license.

  Figure 11. Diagnostics buffer[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/WfohIPR5WjWQJMQY8~nMsg-VBkTPlmjVZAl17lebjV9hA/content?v=cec2dd89713e19c9)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/WfohIPR5WjWQJMQY8~nMsg-VBkTPlmjVZAl17lebjV9hA)
- In the case of a missing or incorrect registration key, the CPU processes the Modbus TCP communication; however, the CPU always displays "W#16#0A90" (No valid license key for functional package) at the STATUS\_x output. The LICENSED output bit is FALSE.

## Input parameters: MB\_MODE, MB\_DATA\_ADDR, MB\_DATA\_LEN, and MB\_DATA\_PTR

The combination of the MB\_MODE, MB\_DATA\_ADDR, and MB\_DATA\_LEN parameters defines the function code used in the current Modbus message:

- **MB\_MODE**contains the information on whether to read or to write:

  **Read**: MB\_MODE = 0, 101, 102, 103 and 104

  **Write**: MB\_MODE = 1, 2, 105, 106, 115 and 116 (Note: With MB\_MODE = 2, there is not distinction between Modbus functions 15 and 05 or between Modbus functions 16 and 06.)
- **MB\_DATA\_ADDR**contains the information on what is to be read or written, as well as address information from which the MB\_RED\_CLIENT instruction calculates the remote address.
- **MB\_DATA\_LEN** contains the number of values to be read/written.

The following table shows the relationship between the input parameters MB\_MODE, MB\_DATA\_ADDR, MB\_DATA\_LEN of the MB\_RED\_CLIENT instruction and the Modbus function:

| **MB\_MODE** | **MB\_DATA\_ADDR** | **MB\_DATA\_LEN** | **Modbus function** | **Function and data type** |
| --- | --- | --- | --- | --- |
| 0 | 1 to 9,999 | 1 to 2,000 | 01 | Read 1 to 2,000 output bits on the remote address 0 to 9,998 |
| 0 | 10,001 to 19,999 | 1 to 2,000 | 02 | Read 1 to 2,000 input bits on the remote address 0 to 9,998 |
| 0 | - 40,001 to 49,999 - 400,001 to 465,535 | 1 to 125 | 03 | - Read 1 to 125 holding registers on the remote address 0 to 9,998 - Read 1 to 125 holding registers on the remote address 0 to 65,534 |
| 0 | 30,001 to 39,999 | 1 to 125 | 04 | Read 1 to 125 input words on the remote address 0 to 9,998 |
| 1 | 1 to 9,999 | 1 | 05 | Write 1 output bit on the remote address 0 to 9,998 |
| 1 | - 40,001 to 49,999 - 400,001 to 465,535 | 1 | 06 | - Write 1 holding register on the remote address 0 to 9,998 - Write 1 holding register on the remote address 0 to 65,534 |
| 1 | 1 to 9,999 | 2 to 1,968 | 15 | Write 2 to 1,968 output bits on the remote address 0 to 9,998 |
| 1 | - 40,001 to 49,999 - 400,001 to 465,535 | 2 to 123 | 16 | - Write 2 to 123 holding registers on the remote address 0 to 9,998 - Write 2 to 123 holding registers on the remote address 0 to 65,534 |
| 2 | 1 to 9,999 | 1 to 1,968 | 15 | Write 1 to 1,968 output bits on the remote address 0 to 9,998 |
| 2 | - 40,001 to 49,999 - 400,001 to 465,535 | 1 to 123 | 16 | - Write 1 to 123 holding registers on the remote address 0 to 9,998 - Write 1 to 123 holding registers on the remote address 0 to 65,534 |
| 11 | The instruction does not evaluate the MB\_DATA\_ADDR and MB\_DATA\_LEN parameters when this function is executed. | | 11 | Read status word and event counter of the server:   - The status word reflects the processing status (0 - not processing, 0xFFFF - processing). - The event counter is incremented when the Modbus request was executed successfully. If an error occurred during execution of a Modbus function, a message is sent by the server but the event counter is not incremented. |
| 80 | - | 1 | 08 | Check the server status with the diagnostic code 0x0000 (return loop test - the server sends the request back):  1 WORD per call |
| 81 | - | 1 | 08 | Reset the event counter of the server with the diagnostic code 0x000A:  1 WORD per call |
| 101 | 0 to 65,535 | 1 to 2,000 | 01 | Read 1 to 2,000 output bits on the remote address 0 to 65,535 |
| 102 | 0 to 65,535 | 1 to 2,000 | 02 | Read 1 to 2,000 input bits on the remote address 0 to 65,535 |
| 103 | 0 to 65,535 | 1 to 125 | 03 | Read 1 to 125 holding registers on the remote address 0 to 65,535 |
| 104 | 0 to 65,535 | 1 to 125 | 04 | Read 1 to 125 input words on the remote address 0 to 65,535 |
| 105 | 0 to 65,535 | 1 | 05 | Write 1 output bit on the remote address 0 to 65,535 |
| 106 | 0 to 65,535 | 1 | 06 | Write 1 holding register on the remote address 0 to 65,535 |
| 115 | 0 to 65,535 | 1 to 1,968 | 15 | Write 1 to 1,968 output bits on the remote address 0 to 65,535 |
| 116 | 0 to 65,535 | 1 to 123 | 16 | Write 1 to 123 holding registers on the remote address 0 to 65,535 |
| 3 to 10,  12 to 79,  82 to 100,  107 to 114,  117 to 255 |  |  |  | Reserved |

Example:

| **Tag** | **Meaning** |
| --- | --- |
| MB\_MODE = 1  MB\_DATA\_ADDR = 1  MB\_DATA\_LEN = 1 | Writes 1 output bit with function code 5, starting from the remote address 0. |
| MB\_MODE = 1  MB\_DATA\_ADDR = 1  MB\_DATA\_LEN = 2 | Writes 2 output bits with function code 15, starting from the remote address 0. |
| MB\_MODE = 104  MB\_DATA\_ADDR = 17834  MB\_DATA\_LEN = 125 | Reads 125 input words with function code 4, starting from the remote address 17.834. |

**MB\_DATA\_PTR**:

The MB\_DATA\_PTR parameter is a pointer to a data buffer for the data to be received from the Modbus server or to be sent to the Modbus server. You can use a global data block or a memory area (M) as the data buffer.

For a buffer in the memory area (M), use a pointer in the ANY format as follows: P#"bit address" "data type" "length" (example: P#M1000.0 WORD 500)

Depending on the memory area in which the data buffer is located, MB\_DATA\_PTR can reference different data structures:

- When you use a global DB with optimized access, MB\_DATA\_PTR can reference a tag with elementary data type or an array of elementary data types. The following data types are supported:

  | **Data type** | **Length in bits** |
  | --- | --- |
  | Bool | 1 |
  | Byte, SInt, USInt, Char | 8 |
  | Word, Int, WChar, UInt | 16 |
  | DWord, DInt, UDInt, Real | 32 |

  You can use all supported data types for all Modbus functions. For example, MB\_RED\_CLIENT can also write a received bit in a tag of the byte type to a specified address without changing other bits in this byte. Therefore, it is not necessary to have an array of bits in order to execute bit-oriented functions.
- If you use a bit memory address area or a global DB with standard access as memory area, there is no longer any restriction to the elementary data types for MB\_DATA\_PTR; MB\_DATA\_PTR can then also reference complex data structures such as PLC data types (UDTs) and system data types (SDTs).

Note:

**Using a bit memory address area as data buffer**

If you use a bit memory address area as data buffer for MB\_DATA\_PTR, you need to observe this variable. With the S7-1200 CPUs, it is 8 KB.

## Output parameters: STATUS\_x, RED\_ERR\_S7, RED\_ERR\_DEV, and TOT\_COM\_ERR

The CPU displays error messages at the status outputs of the MB\_RED\_CLIENT instruction:

Note:

You can display the error status codes as integer or hexadecimal values in the program editor:

1. Open the desired block in the programming editor.
2. Switch on the programming status by clicking "Monitor on/off". (If you have not already established an online connection, the "Go online" dialog opens. In this dialog, you can establish an online connection.)
3. Select the tag that you want to monitor and select the desired display format in the shortcut menu under "Display format".

- STATUS\_x parameter (general status information):

  | **STATUS (W#16#)** | **Description** |
  | --- | --- |
  | 0000 | Instruction executed without errors. |
  | 0001 | Connection established. |
  | 0003 | Connection terminated. |
  | 0A90 | The instruction MB\_RED\_CLIENT is not licensed. Refer to the "Licensing" section above for further information. |
  | 0AFF | The connection is not configured and is not used. The connection "0A" must be configured. |
  | 7000 | No job active and no connection established (REQ=0, DISCONNECT=1). |
  | 7001 | Connection establishment triggered. |
  | 7002 | Intermediate call. Connection is being established. |
  | 7003 | Connection is being terminated. |
  | 7004 | Connection established and monitored. No job processing active. |
  | 7005 | Data is being sent. |
  | 7006 | Data is being received. |
- STATUS\_x parameter (protocol error)

  | **STATUS (W#16#)** | **Description** |
  | --- | --- |
  | 80C8 | No response of the server in the defined period. Check the connection to the Modbus server. This error is only reported on completion of the configured repeated attempts.  If the MB\_RED\_CLIENT instruction does not receive an answer with the originally transferred transaction ID (see static tag MB\_TRANSACTION\_ID) within the defined period, this error code is output. |
  | 8380 | Received Modbus frame has incorrect format or too few bytes were received. |
  | 8382 | - The length of the Modbus frame in the frame header does not match the number of received bytes. - The number of bytes does not match the number of actually transmitted bytes (only functions 1-4). - The start address in the received frame does not match the saved start address (functions 5, 6, 15, and 16). - The number of words does not match the number of actually transmitted words (functions 15 and 16). |
  | 8383 | Error reading or writing data or access outside the address area of MB\_DATA\_PTR. Refer to the "MB\_DATA\_PTR" section above for further information. |
  | 8384 | - Invalid exception code received. - A different data value was received than was originally sent by the client (functions 5, 6, and 8) - Invalid status value received (function 11) |
  | 8385 | - Diagnostics code not supported. - A different subfunction code was received than was originally sent by the client (function 8). |
  | 8386 | Received function code does not match the one sent originally. |
  | 8387 | The protocol ID of the Modbus TCP frame received by the server is not "0". |
  | 8388 | The Modbus server sent a different data length than was processed. This error occurs only when using the Modbus functions 5, 6, 15, or 16. |
- STATUS\_x parameter (parameter error)

  | **STATUS (W#16#)** | **Description** |
  | --- | --- |
  | 80B6 | Invalid connection type; only TCP connections are supported. |
  | 80BB | The ActiveEstablished parameter has an invalid value. Only active connection establishment permitted for client (ActiveEstablished = TRUE). |
  | 8188 | The MB\_MODE parameter has an invalid value. |
  | 8189 | Invalid addressing of data at the MB\_DATA\_ADDR parameter |
  | 818A | Invalid data length at the MB\_DATA\_LEN parameter |
  | 818B | The MB\_DATA\_PTR parameter has an invalid pointer. You should also check the values of the MB\_DATA\_ADDR and MB\_DATA\_LEN parameters. (Refer to the "MB\_DATA\_ADDR" section above for further information on the "MB\_DATA\_ADDR".) |
  | 818C | Timeout at parameter BLOCKED\_PROC\_TIMEOUT or RCV\_TIMEOUT (see static tags of instruction). BLOCKED\_PROC\_TIMEOUT and RCV\_TIMEOUT must be between 0.5 s and 55.0 s. |
  | 8200 | - The CPU is currently processing a different Modbus request through the port. - Another instance of MB\_RED\_CLIENT with the same connection parameters is processing an existing Modbus request. |

Note:

**Error codes of internally used communication instructions**

With the MB\_RED\_CLIENT instruction, in addition to the errors listed in the tables, errors caused by the communication instructions (TCON, TDISCON, TSEND, TRCV, T\_DIAG, and TRESET), used by the instruction, can occur.

The CPU assigns the error codes through the instance data block of the MB\_RED\_CLIENT instruction. The CPU displays the error codes for the respective instruction under STATUS in the "Static" section.

The meaning of the error codes is available in the documentation of the corresponding communications instruction.

Note:

**Communication error when sending or receiving data**

If a communication error occurs when sending or receiving data, the CPU terminates the existing condition. Errors are as follows:

- 80C4 - Temporary communications error; the specified connection is temporarily terminated.
- 80C5 - The remote partner has actively terminated the connection.
- 80A1 - The specified connection is disconnected or is not yet established.

This means that you can see all returned STATUS values when the connection is terminated and that the STATUS code that caused the connection to be terminated is only output when the connection is terminated.

Example: If a temporary communication error occurs when data is received, the STATUS 7003 (ERROR=false) is output initially and then 80C4 (ERROR=true).

---

##### MB_RED_SERVER (Communicating over PROFINET as a Modbus TCP server)

You can use this instruction to establish a connection between an S7-1200 CPU and a device that supports the Modbus TCP protocol.

Table 1. MB\_RED\_SERVER instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"MB\_RED\_SERVER\_DB"(    DISCONNECT:=\_bool\_in\_,    LICENSED=>\_bool\_out\_    IDENT\_CODE=>\_string\_out\_    DR\_NDR\_0A=>\_bool\_out,    ERROR\_0A=>\_bool\_out,    STATUS\_0A=>\_word\_out\_,    DR\_NDR\_1A=>\_bool\_out,    ERROR\_1A=>\_bool\_out,    STATUS\_1A=>\_word\_out\_,    DR\_NDR\_0B=>\_bool\_out,    ERROR\_0B=>\_bool\_out,    STATUS\_0B=>\_word\_out\_,    DR\_NDR\_1B=>\_bool\_out,    ERROR\_1B=>\_bool\_out,    STATUS\_1B=>\_word\_out\_,    RED\_ERR\_S7=>\_bool\_out\_,    RED\_ERR\_DEV=>\_bool\_out\_,    TOT\_COM\_ERR=>\_bool\_out\_,    MB\_HOLD\_REG:=\_variant\_inout\_);** | The MB\_RED\_SERVER instruction communicates as a Modbus TCP server over the PROFINET connection.  The instruction MB\_RED\_SERVER processes connection requests of a Modbus TCP client, receives and processes Modbus requests, and sends responses. |

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REG\_KEY 1 | IN | STRING[17] | Registration code for licensing  The MB\_RED\_SERVER instruction must be licensed on each CPU individually. |
| DISCONNECT | IN | Bool | You use the MB\_RED\_SERVER instruction to enter into a passive connection with a partner module. The server responds to a connection request from the IP addresses which are given in the connection descriptions as specified or unspecified.  You can use this parameter to control when a connection request is accepted:   - 0: The CPU establishes a passive connection when there is no communications connection. - 1: Initialization of the connection termination. If the input is set, the CPU processes no additional client requests, and termination of the connection is initiated. The value "0003" is output at the STATUS\_x parameter after successful connection termination. |
| MB\_HOLD\_REG 2 | IN\_OUT | Variant | Pointer to the Modbus holding register of the MB\_RED\_SERVER instruction  MB\_HOLD\_REG must always reference a memory area that is larger than two bytes.  The holding register contains the values that a Modbus client can access by using the Modbus functions 3 (read), 6 (write), 16 (multiple write), and 23 (reading and writing in one job). |
| LICENSED 1 | OUT | Bool | - 0: Instruction is not licensed - 1: Instruction is licensed |
| IDENT\_CODE 1 | OUT | STRING[18] | Identification for licensing. Use this string to request the REG\_KEY registration code. |
| DR\_NDR\_0A | OUT | Bool | "Data Read" or "New Data Ready" to connection 0A:   - 0: No new data - 1: New data read or written by the Modbus client |
| ERROR\_0A | OUT | Bool | If an error occurs during a call of the MB\_RED\_SERVER instruction to connection 0A, the output of the ERROR\_0A parameter is set to "1". Detailed information about the cause of the problem is indicated by the STATUS\_0A parameter. |
| STATUS\_0A 3 | OUT | Word | Detailed status information of the instruction on connection 0A. |
| DR\_NDR\_1A | OUT | Bool | "Data Read" or "New Data Ready" to connection 1A:   - 0: No new data - 1: New data read or written by the Modbus client |
| ERROR\_1A | OUT | Bool | If an error occurs during a call of the MB\_RED\_SERVER instruction to connection 1A, the output of the ERROR\_1A parameter is set to "1". Detailed information about the cause of the problem is indicated by the STATUS\_1A parameter. |
| STATUS\_1A 3 | OUT | Word | Detailed status information of the instruction on connection 1A. |
| DR\_NDR\_0B | OUT | Bool | "Data Read" or "New Data Ready" to connection 0B:   - 0: No new data - 1: New data read or written by the Modbus client |
| ERROR\_0B | OUT | Bool | If an error occurs during a call of the MB\_RED\_SERVER instruction to connection 0B, the output of the ERROR\_0B parameter is set to "1". Detailed information about the cause of the problem is indicated by the STATUS\_0B parameter. |
| STATUS\_0B 3 | OUT | Word | Detailed status information of the instruction on connection 0B. |
| DR\_NDR\_1B | OUT | Bool | "Data Read" or "New Data Ready" to connection 1B:   - 0: No new data - 1: New data read or written by the Modbus client |
| ERROR\_1B | OUT | Bool | If an error occurs during a call of the MB\_RED\_SERVER instruction to connection 1B, the output of the ERROR\_1B parameter is set to "1". Detailed information about the cause of the problem is indicated by the STATUS\_1B parameter. |
| STATUS\_1B 3 | OUT | Word | Detailed status information of the instruction on connection 1B. |
| RED\_ERR\_S7 3 | OUT | Bool | - 0: No redundancy error in SIMATIC - 1: Redundancy error in SIMATIC |
| RED\_ERR\_S7 3 | OUT | Bool | - 0: No redundancy error on side of link partner - 1: Redundancy error on side of link partner |
| RED\_ERR\_S7 3 | OUT | Bool | - 0: At least 1 configured connection is established - 1: Complete loss of communication, all configured connections are terminated |

1 Refer to the "Licensing" section below for further information.

2 Refer to the "MB\_HOLD\_REG input parameter" section below for further information.

3 Refer to the "Output parameters: ERROR\_x, RED\_ERR\_S7, RED\_ERR\_DEV, and TOT\_COM\_ERR" section below for further information.

Warning:

**Risks with access to the process image**

Each Modbus TCP client has read and write access to the process image inputs and outputs, and to the data block or bit memory area defined by the Modbus holding register. Unauthorized read and write operations can change PLC variables into invalid values and disrupt process operations.

To reduce the risk of unauthorized access, restrict access to an IP address of a specific Modbus client. For information on additional industrial security measures that can be implemented, please visit the [Siemens Industrial Cybersecurity Web site](https://www.siemens.com/global/en/products/automation/topic-areas/industrial-cybersecurity.html).

Disruption of process operations can result in death, severe injury and/or property damage.

## Multiple server connections

The CPUs can:

- Process multiple server connections
- Accept multiple connections from different clients, simultaneously, at one server port

The maximum number of connections depends on the CPU being used and can be found in the technical specifications of the CPU. The total number of connections of one CPU, including those of the Modbus TCP clients and server must not exceed the maximum number of supported connections.

In the case of server connections, remember the following rules:

- Each MB\_RED\_SERVER connection must use a unique instance DB.
- One unique connection/connection ID is required for each and every client that wants to connect to the server port.
- The connection IDs must be unique throughout the CPU.

## Mapping of Modbus addresses to the process image

The MB\_RED\_SERVER instruction allows incoming Modbus functions (1, 2, 4, 5, and 15) direct read and write access to the process image inputs and outputs of the CPU (use of the data types BOOL and WORD).

For S7-1200-CPUs, the address space for the process image of the inputs and the process image of the outputs is 1 KB.

The following table shows the address space of the Modbus functions listed above:

| **Modbus function** | | | | | |
| --- | --- | --- | --- | --- | --- |
| **Function code** | **Function** | **Data area** | **Address space** | | |
| 01 | Read: Bits | Output | 0 | to | 65.535 |
| 02 | Read: Bits | Input | 0 | to | 65.535 |
| 04 | Read: WORD | Input | 0 | to | 65.535 |
| 05 | Write: Bit | Output | 0 | to | 65.535 |
| 15 | Write: Bits | Output | 0 | to | 65.535 |

Incoming Modbus requests with the function codes 3, 6, 16, and 23 write or read the Modbus holding registers (you specify the holding register with the MB\_HOLD\_REG parameter or using Data\_Area\_Array).

## Modbus functions

The following table lists all the Modbus functions that are supported by the MB\_RED\_SERVER instruction:

| **Function code** | **Description** |
| --- | --- |
| 01 | Read output bits |
| 02 | Read input bits |
| 03 | Read a holding register |
| 04 | Read input words |
| 05 | Write an output bit |
| 06 | Write a holding register |
| 08 | Diagnostics function:   - Echo test (subfunction 0x0000): The MB\_RED\_SERVER instruction receives a data word and returns this unchanged to the Modbus client. - Reset event counter (subfunction 0x000A): The MB\_RED\_SERVER instruction resets the following event counters: "Success\_Count", "Xmt\_Rcv\_Count", "Exception\_Count", "Server\_Message\_Count", and "Request\_Count". |
| 11 | Diagnostics function: Fetch event counter of the communication  The MB\_RED\_SERVER instruction uses an internal event counter for communication to record the number of successfully executed read and write requests sent to the Modbus server.  The event counter is not incremented with the functions 8 or 11. The same holds true for requests that cause a communications error, for example, if a protocol error has occurred; the function code in the received Modbus request is not supported). |
| 15 | Write output bits |
| 16 | Write a holding register |
| 23 | Write a holding register and read a holding register with a request |

## Operation and redundancy

The communication nodes can be designed as standalone or redundant. If one of the partners is designed as standalone, we refer to it as single-sided redundancy. If both partners are designed redundantly, we refer to it as double-sided redundancy.

- Single-sided redundancy:

  - One connection each must be configured for each connection between the communication partners. The connection points of the **SIMATIC S7** are referred to as **0** and **1**; the connection points of the **communication partner** are referred to as **A** and **B**.

    The R-CPU or H-CPU 1 refers to the connection point 0, the R-CPU or H-CPU 2 refers to the connection point 1.
  - Configuration: If the S7 is designed redundantly, one connection is created from the S7 connection point 0 to junction A of the link partner (Connection from the S7 connection point **0** to the partner/node **A** => connection **0A**), and one connection from the S7 connection point 1 to junction A of the link partner (Connection from the S7 connection point **1** to the partner/node **A** => connection **1A**). The figure illustrates the connection designations:

    Figure 1. Single-sided redundancy S7[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/YFxUioGjR_CKtPDfRi4cpg-VBkTPlmjVZAl17lebjV9hA/content?v=d6bbb42c55865cc1)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/YFxUioGjR_CKtPDfRi4cpg-VBkTPlmjVZAl17lebjV9hA)
  - If the S7 is designed as standalone and the link partner is designed redundantly, one connection is created from the S7 connection point 0 to junction A of the link partner (connection from the S7 connection point **0** to the partner/node **A** => connection **0A**), and one connection from the S7 connection point 0 to junction B of the link partner (connection from the S7 connection point **0** to the partner/node **B** => connection **0B**). The figure illustrates the connection designations:

    Figure 2. Single-sided redundancy partner[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/z6xvjZ1xJOBS7W8E_xZqUw-VBkTPlmjVZAl17lebjV9hA/content?v=880f903dc24f2a46)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/z6xvjZ1xJOBS7W8E_xZqUw-VBkTPlmjVZAl17lebjV9hA)
- Double-sided redundancy:

  - Description: One connection each must be configured for each connection between the communication partners. The connection points of the SIMATIC S7 are referred to as **0** and **1**; the connection points of the **communication partner** are referred to as **A** and **B**.

    The R-CPU or H-CPU 1 refers to the connection point 0, the R-CPU or H-CPU 2 refers to the connection point 1.
  - Configuration: In the case of double-sided redundancy, two connections are created from connection point 0 (connection from the S7 connection point **0** to the partner/node **A** => connection **0A** and connection from the S7 connection point **0** to the partner/node **B** => connection **0B**), and two connections from connection point 1 of the S7 to the junctions A and B of the link partner (connection from the S7 connection point **1** to the partner/node **A** => connection **1A** and connection from the S7 connection point **1** to the partner/node **B** => connection **1B**). The figure illustrates the connection designations:

    Figure 3. Double-sided redundancy[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/uDUvJ9Cv2SmQqeHbJTtcKA-VBkTPlmjVZAl17lebjV9hA/content?v=fce3149035ccfe48)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/uDUvJ9Cv2SmQqeHbJTtcKA-VBkTPlmjVZAl17lebjV9hA)
- Frame processing: Frames can be received through all configured connections. The client can send frames either through one connection or through all connections. If a frame was received on a connection, the CPU displays the status at the corresponding output DR\_NDR\_x or ERROR\_x. Each connection runs independently and has no influence on the display of the other connections.
- Redundancy outputs RED\_ERR\_S7, RED\_ERR\_DEV, and TOT\_COM\_ERR:

  - The redundancy bits RED\_ERR\_S7, RED\_ERR\_DEV, and TOT\_COM\_ERR are set based on the states of the status outputs:

    Figure 4. Display of the interrupt bits for redundancy setup on both sides[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/bWD67_LXVkIXYY0rDDTv0A-VBkTPlmjVZAl17lebjV9hA/content?v=42bff8eb824525d9)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/bWD67_LXVkIXYY0rDDTv0A-VBkTPlmjVZAl17lebjV9hA)

    Figure 5. Display of the interrupt bits for redundancy setup on one side[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/VBLO6ke8AddG5fXgwrxipg-VBkTPlmjVZAl17lebjV9hA/content?v=d5233145ed3f00d0)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/VBLO6ke8AddG5fXgwrxipg-VBkTPlmjVZAl17lebjV9hA)

Note:

**Port numbers for client and server**

The Modbus client uses a port number starting at 2000. The Modbus server is usually addressed over the port number 502. Depending on the CPU, it is possible to configure port 502 for multiple connections (Multiport). If the local port 502 was configured for two or more connections, the requesting clients are randomly distributed to the existing server connections in the case of unspecified connections. The first client that wants to connect to the "MB\_RED\_SERVER" instruction is not automatically assigned the connection 0A. Once the assignment of the client requests to the server connections has taken place, the assignment remains intact during the frame exchange until the connection is terminated.

## Parameter assignment

You can use the MB\_RED\_SERVER instruction **V1.0** and **V1.1** for S7-1200. The CPU implements the connections over the local interface of the CPU or CM/CP. The CPU configures and establishes the connections using the TCON\_IP\_V4 structure.

Configuration of MB\_RED\_SERVER: You make the following settings using the configuration dialog of the MB\_RED\_SERVER instruction:

- Connection parameters for the connections 0A, 1A, 0B and 1B (Refer to "Operation and Redundancy", above, for more information on redundancy configuration.)
- Internal parameter (optional)

You can open the configuration dialog with the MB\_RED\_SERVER instruction or through the technology objects:

Figure 6. Parameterized server connection[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/a9ZuOXrQMw3~~WSzTOisvg-VBkTPlmjVZAl17lebjV9hA/content?v=b919940980a256d9)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/a9ZuOXrQMw3~~WSzTOisvg-VBkTPlmjVZAl17lebjV9hA)

Figure 7. Configured server connection[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/D7QfwFF~hC0axwW2X~9W9w-VBkTPlmjVZAl17lebjV9hA)

| **Tag** | **Start value** | **Description** |
| --- | --- | --- |
| **Configured connections** | | |
| Interface ID | 64 | HW identifier of the PN interface used |
| Connection ID | 16#0000 | Connection IDs for the connections used. These connection IDs must be unique throughout the CPU. |
| Local port | 502 | Local port number of the server block. The default port for Modbus/TCP server is 502. |
| Remote IP | 0.0.0.0 | Remote IP address of the client. By default, no IP address is entered for the client. |
| Remote port | 0 | Remote port number of the client. By default, no port number is entered for the client. |
| **Configured connections** | | |
| Interface ID | 64 | HW identifier of the PN interface used |
| Connection ID | 16#0000 | Connection IDs for the connections used. These connections are configured in the network view. |

Figure 8. Internal parameter (optional)[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/fT32BRBCG_gtEH6R4BvVCQ-VBkTPlmjVZAl17lebjV9hA/content?v=85bba1198b7fa1a6)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/fT32BRBCG_gtEH6R4BvVCQ-VBkTPlmjVZAl17lebjV9hA)

| **Tag** | **Data type** | **Start value** | **Description** |
| --- | --- | --- | --- |
| HR\_Start\_Offset | WORD | 0 | Assign the start address of the Modbus holding register. |
| QB\_Start | UINT | 0 | Start address of the permitted addressing range of the outputs that the Modbus master can write to (bytes 0 to 65535) |
| QB\_Count | UINT | 0 | Number of output bytes that the Modbus master can write to.  *Example:*   - QB\_Start=0 and QB\_Count=10: The Modbus master can write to output bytes 0 to 9. - QB\_Count=0: The Modbus master cannot write to any output byte. |
| QB\_Read\_Start | UINT | 0 | Start address of the permitted addressing range of the outputs that the Modbus master can read (bytes 0 to 65535) |
| QB\_Read\_Count | UINT | 0 | Number of output bytes that the Modbus master can read.  *Example:*   - QB\_Read\_Start=0 and QB\_Read\_Count=10: The Modbus master can read output bytes 0 to 9. - QB\_Read\_Count=0: The Modbus master cannot read any output byte. |
| IB\_Read\_Start | UINT | 0 | Start address of the permitted addressing range of the inputs that the Modbus master can read (bytes 0 to 65535) |
| IB\_Read\_Count | UINT | 0 | Number of input bytes that the Modbus master can read.  *Example:*  IB\_Read\_Start=0 and IB\_Read\_Count=10: The Modbus master can read input bytes 0 to 9.  IB\_Read\_Count=0: The Modbus master cannot read any input byte. |
| Data\_Area\_Array | ARRAY [1..8] | |  |
| data\_type | UINT | 0 | Data Type: 0 to 4 |
| db | UINT | 0 | Data block number |
| start | UINT | 0 | First Modbus address in the data block |
| length | UINT | 0 | Number of Modbus values in the data block |

**Addressing using the** **HR\_Start\_Offset** **static tag**

The addresses of the Modbus holding register start at 0.

*Example:* The holding register begins at MW100 and has a length of 100 words.

Figure 9. HR\_Start\_Offset\_0[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/32slfcRlgtdPeeLHhgtp6A-VBkTPlmjVZAl17lebjV9hA)

You can define the HR\_Start\_Offset tag so that the Modbus holding register has a start address other than 0.

*Example:* An offset value of 20 in the HR\_Start\_Offset parameter means that the start address of the holding register is moved from 0 to 20. This causes an error whenever you address the holding register below the address 20 and above the address 119.

Figure 10. HR\_Start\_Offset\_20[![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/Zsmxwf0Ihr1qBYSAWBhLNw-VBkTPlmjVZAl17lebjV9hA)

**Data\_Area\_Array [1..8]**

There are eight data areas available for mapping the MODBUS addresses in the SIMATIC S7 memory. If the data area is defined with the "Holding Register" data type, the MB\_HOLD\_REG parameter is not evaluated. Instead, the Modbus master writes or reads the Modbus register and bits in the data blocks depending on the job type. The CPU can further process these values in the subsequent execution of the program.

Figure 11. Server data areas[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/mY9KQEEaS6kK7sYxxY2j2Q-VBkTPlmjVZAl17lebjV9hA/content?v=1fe582c1e7819dea)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/mY9KQEEaS6kK7sYxxY2j2Q-VBkTPlmjVZAl17lebjV9hA)

You can only read from one DB or write to one DB with any job. Access to registers or bit values that are located in several DBs, even if the numbers are in a sequence without gaps, are to be divided into two jobs. Keep this in mind during configuration. It is possible to map more Modbus areas (registers or bit values) in one data block than the Modbus master can process with one frame.

**data\_type**

The data\_type parameter specifies which MODBUS data types the Modbus master maps in this data block. If the value "0" is entered in data\_type, the Modbus master does not use the corresponding data area. If the Modbus master is to use multiple Data\_Area, you must define these one after the other. The Modbus master does not process any entries after a data\_type = 0.

| **Identifier** | **Data type** | **Description** |
| --- | --- | --- |
| 0 | Area not used |  |
| 1 | Output bits (Coils) | Bit |
| 2 | Input bits (Inputs) | Bit |
| 3 | Holding register | Word |
| 4 | Input words (Input Register) | Word |

**db**

The db parameter specifies the data block which maps the MODBUS registers or bit values defined below. The CPU does not permit the DB number 0 because it is reserved for the system.

**start, length**

start specifies the first Modbus address which the Modbus master maps in data word 0 of the DB. The parameter length defines the length of how many MODBUS addresses the Modbus master maps in the data block. The defined data areas must not overlap. The length parameter must not be 0.

**Example: Address mapping with** **Data\_Area\_Array**

|  |  |  |
| --- | --- | --- |
| Data area 1 | data\_type | 3: Holding register |
| db | 11 |
| start | 0 |
| length | 500 |
| Data area 2 | data\_type | 3: Holding register |
| db | 12 |
| start | 720 |
| length | 181 |
| Data area 3 | data\_type | 4: Input words |
| db | 13 |
| start | 720 |
| length | 281 |
| Data area 4 | data\_type | 1: Output bits |
| db | 14 |
| start | 640 |
| length | 611 |
| Data area 5 | data\_type | 2: Input bit |
| db | 15 |
| start | 1700 |
| length | 601 |
| Data area 6 | data\_type | 1: Output bits |
| db | 16 |
| start | 1700 |
| length | 601 |
| Data area 7 | data\_type | Not used |
| db | 0 |
| start | 0 |
| length | 0 |
| Data area 8 | data\_type | Not used |
| db | 0 |
| start | 0 |
| length | 0 |

Figure 12. Address building[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/Bj1nqx3SW8gDHCnLSyfUcQ-VBkTPlmjVZAl17lebjV9hA/content?v=52e6e011a3228675)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/Bj1nqx3SW8gDHCnLSyfUcQ-VBkTPlmjVZAl17lebjV9hA)

## Licensing

The MB\_RED\_SERVER instruction is subject to a fee, and you must license the instruction on each CPU individually. Licensing takes place in two steps:

- Displaying the license IDENT\_CODE
- Entering the REG\_KEY registration key: You must assign the REG\_KEY registration key at each MB\_RED\_SERVER instruction. Save the REG\_KEY in a global data block from which all MB\_RED\_SERVER instructions receive the necessary registration key.

Procedure for displaying the license IDENT\_CODE:

1. Assign parameters to the MB\_RED\_SERVER instruction in line with your requirements in a cyclic OB. Download the program to the CPU and set the CPU to RUN.
2. Open the instance DB of the Modbus instruction, and click the "Monitor all" button.
3. The instance DB displays an 18-digit character string at the IDENT\_CODE output.

   Figure 13. License[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/0qaxC9yCwDBYgNl0vvLaew-VBkTPlmjVZAl17lebjV9hA/content?v=bc5395163158b154)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/0qaxC9yCwDBYgNl0vvLaew-VBkTPlmjVZAl17lebjV9hA)
4. Copy this string using copy/paste from the data block and paste it in the form (that was sent to you by email after you ordered the product or is included on the CD).
5. Send the form to [Customer support](https://support.industry.siemens.com/my/ww/en/requests/) using a service request. You will then receive the registration key for your CPU.

Procedure for entering the registration key REG\_KEY:

1. Insert a new global data block with a unique symbolic name, for example "License\_DB", using "Add new block…".
2. Create a REG\_KEY parameter in this block with the data type STRING[17].

   Figure 14. REG\_KEY[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/T85Qf2eNVUgW_Qi1nvru7w-VBkTPlmjVZAl17lebjV9hA/content?v=8c6ba9deed873cd9)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/T85Qf2eNVUgW_Qi1nvru7w-VBkTPlmjVZAl17lebjV9hA)
3. Copy the transmitted 17-digit registration key using copy/paste to the "Start value" column.
4. In the cyclic OB, enter the name of the license DB and the name of the string (for example, License\_DB.REG\_KEY) at the REG\_KEY parameter of the MB\_RED\_SERVER instruction.
5. Download the modified blocks to the CPU. You can enter the registration key during runtime; a change from STOP to RUN is not necessary.
6. The Modbus/TCP communication using the MB\_RED\_SERVER instruction is now licensed for this CPU; the LICENSED output bit is TRUE.

Procedure for correcting missing or incorrect licensing:

- If you enter an incorrect registration key or no registration key, the ERROR LED of the CPU flashes. In addition, for the S7-1200, the CPU makes a cyclic entry in the diagnostics buffer regarding the missing license.

  Figure 15. Diagnostic\_buffer[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/WfohIPR5WjWQJMQY8~nMsg-VBkTPlmjVZAl17lebjV9hA/content?v=cec2dd89713e19c9)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/WfohIPR5WjWQJMQY8~nMsg-VBkTPlmjVZAl17lebjV9hA)
- In the case of a missing or incorrect registration key, the CPU processes the Modbus TCP communication; however, the CPU always displays "W#16#0A90" (No valid license key for functional package) at the STATUS\_x output. The LICENSED output bit is FALSE.

## MB\_HOLD\_REG input parameter

The MB\_HOLD\_REG parameter is a pointer to a data buffer for storing the data to which a Modbus client has read or write access. You can use a global data block (D) or bit memory (M) as memory area:

- The high limit for the number of addresses in the data block (D) is determined by the maximum size of a DB of your CPU.
- The high limit for the number of bit memories (M) is determined by the maximum bit memory area of your CPU.

The following figures show some examples of mapping Modbus addresses to the holding register for the Modbus functions 3 (read multiple WORD), 6 (write one WORD), 16 (write multiple WORD), and 23 (write and read multiple WORD).

Figure 16. MB\_HOLD\_REG: Data block with offset 0[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/5I7yOFUXjSjIQ2ql3PnP5A-VBkTPlmjVZAl17lebjV9hA/content?v=b66e612b1a28db57)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/5I7yOFUXjSjIQ2ql3PnP5A-VBkTPlmjVZAl17lebjV9hA)

Figure 17. MB\_HOLD\_REG: Data block with offset 60[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/Ccau1ITyjZsRfZW_0LeQyg-VBkTPlmjVZAl17lebjV9hA/content?v=d100ad5517aac0c7)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/Ccau1ITyjZsRfZW_0LeQyg-VBkTPlmjVZAl17lebjV9hA)

**Data\_Area\_Array [1..8]**: To use the optional parameters Data\_Area\_Array [1..8], refer to the "Parameter assignment" section above.

## Output parameters: ERROR\_x, STATUS\_x, RED\_ERR\_S7, RED\_ERR\_DEV, and TOT\_COM\_ERR

The CPU displays error messages at the status outputs of the MB\_RED\_SERVER instruction:

Note:

You can display the error status codes as integer or hexadecimal values in the program editor:

1. Open the desired block in the programming editor.
2. Switch on the programming status by clicking "Monitor on/off". (If you have not already established an online connection, the "Go online" dialog opens. In this dialog, you can establish an online connection.)
3. Select the tag that you want to monitor and select the desired display format in the shortcut menu under "Display format".

STATUS\_x parameter (general status information):

| **STATUS (W#16#)** | **Description** |
| --- | --- |
| 0000 | Instruction executed without errors. |
| 0001 | Connection established. |
| 0003 | Connection terminated. |
| 0A90 | The instruction MB\_RED\_SERVER is not licensed. Refer to the "Licensing" section above for further information. |
| 0AFF | The connection is not configured and is not used. The connection 0A must be configured. |
| 7000 | No call active and no connection established (REQ=0, DISCONNECT=1). |
| 7001 | First call. Connection establishment triggered. |
| 7002 | Intermediate call. Connection is being established. |
| 7003 | Connection is being terminated. |
| 7005 | Data is being sent. |
| 7006 | Data is being received. |

STATUS\_x parameter (protocol error)

| **STATUS (W#16#)** | **Error code in the error message from MB\_RED\_SERVER(B#16#)** | **Description** |
| --- | --- | --- |
| 8380 | - | Received Modbus frame has incorrect format or too few bytes were received. |
| 8381 | 01 | Function code is not supported. |
| 8382 | 03 | Error in data length:   - Invalid length specification in received Modbus frame - The frame length entered in the header of the Modbus frame does not match the number of actually received bytes. - The number of bytes entered in the header of the Modbus frame does not match the number of actually received bytes (functions 15 and 16). |
| 8383 | 02 | Error in data address or access outside the address area of the holding register (MB\_HOLD\_REG parameter). Refer to the "MB\_HOLD\_REG" section above for further information. |
| 8384 | 03 | Error in the data value (function 05) |
| 8385 | 03 | Diagnostic code is not supported (only with function 08). |

STATUS\_x parameter (parameter error)

| **STATUS (W#16#)** | **Description** |
| --- | --- |
| 80BB | The ActiveEstablished parameter has an invalid value  Only passive connection establishment permitted for server (active\_established = FALSE). |
| 8187 | The MB\_HOLD\_REG parameter has an invalid pointer. Data area is too small. |
| 8389 | Invalid data area definition:   - Invalid data\_type value - DB number invalid or does not exist:    - Invalid db value   - DB number does not exist   - DB number is already used by another data area   - DB with optimized access   - DB is not located in the work memory - Invalid length value - Overlapping of MODBUS address ranges that belong to the same MODBUS data type |

Note:

**Error codes of internally used communication instructions**

With the MB\_RED\_SERVER instruction, in addition to the errors listed in the tables, errors caused by the communication instructions ("TCON", "TDISCON", "TSEND", "TRCV", "T\_DIAG" and "T\_RESET") used by the instruction can occur.

The error codes are assigned via the instance data block of the MB\_RED\_SERVER instruction. The error codes are displayed for the respective instruction under STATUS in the "Static" section of the individual instances.

The meaning of the error codes is available in the documentation of the corresponding communications instruction.

Note:

**Communication error when sending or receiving data**

If a communication error occurs when sending or receiving data, the CPU terminates the existing condition. Errors are as follows:

- 80C4 - Temporary communications error; the specified connection is temporarily terminated.
- 80C5 - The remote partner has actively terminated the connection.
- 80A1 - The specified connection is disconnected or is not yet established.

This also means that you can see all STATUS values that are returned when the connection is terminated and that the STATUS code that caused the connection to be terminated is only output when the connection is terminated.

Example: If a temporary communication error occurs when data is received, the STATUS 7003 (ERROR=false) is output initially and then 80C4 (ERROR=true).

---

#### Modbus TCP examples


---

##### Example: MB_SERVER Multiple TCP connections

You can have multiple Modbus TCP server connections. To accomplish this, MB\_SERVER must be independently executed for each connection. Each connection must use an independent instance DB, connection ID, and IP port. The S7-1200 allows only one connection per IP port.

For best performance, MB\_SERVER should be executed every program cycle, for each connection.

The CONNECT parameter uses system data type TCON\_IP\_V4. For the example, these data structures are in a DB named "Modbus connections". The "Modbus connections" DB contains two TCON\_IP\_V4 structures "TCPpassive\_1" (for connection 1) and "TCP\_passive\_2" (for connection 2).The connection properties ID and LocalPort described in the network comments are data elements stored in the CONNECT data structure.

The TCON\_IP\_V4 CONNECT data also contains an IP address in the RemoteAddress ADDR array. IP address assignments within TCPpassive\_1 and TCP\_passive\_2 do not affect the establishment of TCP server connections, but determine which Modbus TCP clients are allowed to communicate though the connections to each MB\_SERVER. MB\_SERVER passively listens for a Modbus client message and compares the incoming message IP address with the IP address stored in the corresponding RemoteAddress ADDR array.

Three MB\_SERVER IP address variations are possible for the two MB\_SERVER instructions:

- **IP address = 0.0.0.0**

  Each MB\_SERVER will respond to all Modbus TCP clients using any IP address.
- **IP address = Same IP address in TCPpassive\_1 and TCPpassive\_2**

  Both MB\_SERVER connections only respond to Modbus clients originating from this IP address.
- **IP address = Different IP number in TCP\_passive\_1 and TCP\_passive\_2**

  Each MB\_SERVER only responds to Modbus clients that originate from the IP address stored in their TCON\_IP\_V4 data.

**Network 1:** Connection #1, Instance DB = "MB\_SERVER\_DB", within "Modbus connections.TCPpassive\_1" (ID = 1 and LocalPort = 502)

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/cbAuY2nyeVFzCLpsAB_8Zg-VBkTPlmjVZAl17lebjV9hA/content?v=b0d54c2131cd3677)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/cbAuY2nyeVFzCLpsAB_8Zg-VBkTPlmjVZAl17lebjV9hA)

**Network 2:** Connection #2, Instance DB = "MB\_SERVER\_DB\_1, within "Modbus connections.TCPpassive\_2" (ID = 2 and LocalPort = 503)

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/olJjWNSweGVZdU3Vvai98Q-VBkTPlmjVZAl17lebjV9hA/content?v=642b6c028ee47aa1)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/olJjWNSweGVZdU3Vvai98Q-VBkTPlmjVZAl17lebjV9hA)

---

##### Example: MB_CLIENT 1: Multiple requests with common TCP connection

Multiple Modbus client requests can be sent over the same connection. To accomplish this, use the same instance DB, connection ID, and port number.

Because both MB\_CLIENT boxes use the same CONNECT parameter TCON\_IP\_v4 data structure ("Modbus\_connections".TCPactive\_1), the connection ID, port number, and IP address are identical. The CONNECT IP address data assigns the IP address, of the target Modbus TCP server.

Only one MB\_CLIENT can be active at any given time. Once a client completes its execution, the next client can begin execution. Your program logic is responsible for the execution sequence logic. The example shows both clients reading remote data from a single Modbus client and transferring the data to the Modbus client's CPU (M memory starting at M1000.0). A returned error is captured, which is optional.

**Network 1:** Modbus function 1 - Read 16 output bits from a Modbus TCP server with the IP address assigned in "Modbus connections".TCPactive\_1.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/UfVglvqdem0Le~4qS9bEhg-VBkTPlmjVZAl17lebjV9hA/content?v=61a2129501599728)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/UfVglvqdem0Le~4qS9bEhg-VBkTPlmjVZAl17lebjV9hA)

**Network 2:** Modbus function 2 - Read 32 input bits from a Modbus TCP server with the IP address assigned in "Modbus connections".TCPactive\_1.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/_HnBheSRwlr2pPmdWGazSw-VBkTPlmjVZAl17lebjV9hA/content?v=b7adf05abfbdbcc4)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/_HnBheSRwlr2pPmdWGazSw-VBkTPlmjVZAl17lebjV9hA)

---

##### Example: MB_CLIENT 2: Multiple requests with different TCP connections

Modbus TCP client requests can be sent over different connections. To accomplish this, different instance DBs and connection IDs must be used.

The RemotePort (IP port) number must be different, if the connections are established to the same Modbus server. If the connections are on different servers, there is no IP port number restriction.

The example shows two Modbus TCP clients transferring remote data from two different Modbus TCP servers to the same local CPU memory area, starting at address M1000.0. Also, a returned error is captured which is optional.

**Network 1:** Modbus function 4 - Read input process image words from a Modbus TCP server

CONNECT parameter = "Modbus connections".TCPactive\_1: Connection **ID** = 1, **RemoteAddress** = 192.168.2.241, **RemotePort** = 502

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/dCXbOjkElDujWckZfusXWA-VBkTPlmjVZAl17lebjV9hA/content?v=9360453c717066ae)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/dCXbOjkElDujWckZfusXWA-VBkTPlmjVZAl17lebjV9hA)

**Network 2:** Modbus function 3 - Read holding register words from a Modbus TCP server

CONNECT parameter = "Modbus connections".TCPactive\_2: Connection **ID** = 2, **RemoteAddress** = 192.168.2.242, **RemotePort** = 502

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/1pCJD4wpjxDnELM27VMEhQ-VBkTPlmjVZAl17lebjV9hA/content?v=d8c8dfb4933b79e8)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/1pCJD4wpjxDnELM27VMEhQ-VBkTPlmjVZAl17lebjV9hA)

---

##### Example: MB_CLIENT 3: Output image write request

This example shows a Modbus client request that transfers bit data from local CPU memory (starting at M1000.0) to a remote Modbus TCP server.

**Network 1:** Modbus function 15 - Write output bits in a Modbus server

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/cp~f2k4vdZid1YBvPAOAyA-VBkTPlmjVZAl17lebjV9hA/content?v=1b14addeb7efc79d)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/cp~f2k4vdZid1YBvPAOAyA-VBkTPlmjVZAl17lebjV9hA)

---

##### Example: MB_CLIENT 4: Coordinating multiple requests

You must ensure that each individual Modbus TCP request finishes execution. The execution sequence must be controlled by your program logic. The example below shows how the outputs of the first and second client requests can control the execution sequence.

The example shows both clients using the same CONNECT connection data (used at different times). The clients transfer holding register data from the same remote Modbus TCP server to the same local CPU memory M address. Also, a returned error is captured which is optional.

**Network 1:** Modbus function 3 - Read Modbus TCP server holding register words

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/z~MXFhRo_OHJEfEakzyfUQ-VBkTPlmjVZAl17lebjV9hA/content?v=646fc144ea81fdb8)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/z~MXFhRo_OHJEfEakzyfUQ-VBkTPlmjVZAl17lebjV9hA)

**Network 2:** Modbus function 3 - Read Modbus TCP server holding register words

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/q6N769ywPqiinLwvssI0Sw-VBkTPlmjVZAl17lebjV9hA/content?v=8b868a4e626b6697)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/q6N769ywPqiinLwvssI0Sw-VBkTPlmjVZAl17lebjV9hA)

---

### Modbus RTU


---

#### Overview

Modbus RTU (Remote Terminal Unit) is a standard network communication protocol that uses the RS232 or RS485 electrical connection for serial data transfer between Modbus network devices. You can add PtP (Point to Point) network ports to a CPU with a RS232 or RS485 CM or a RS485 CB.

Modbus RTU uses a master/slave network where all communications are initiated by a single Master device and slaves can only respond to a master’s request. The master sends a request to one slave address and only that slave address responds to the command.

Modbus RTU enables you to use PROFINET or PROFIBUS distributed I/O to communicate to various devices (RFID readers, GPS device, and others):

- [PROFINET](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Z44~rg1h4WN9JoB7bugZXQ?section=Xa4efc1a7d4610374ba647f805029a400): You connect the Ethernet interface of the S7-1200 CPU to a PROFINET interface module. PtP communication modules in the rack with the interface module can then provide serial communications to external Modbus devices.
- [PROFIBUS](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/bUmtrcn0SdnXwmyXWr7~qA?section=X857a761a79879d39777112eb0d337413): You insert a PROFIBUS communication module in the left side of the rack with the S7-1200 CPU. You connect the PROFIBUS communication module to a rack containing a PROFIBUS interface module. PtP communication modules in the rack with the interface module can then provide serial communications to external Modbus devices.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/7CTIYcD3WOOf2JRKG_mQ0g-VBkTPlmjVZAl17lebjV9hA/content?v=4e77a0be65f7e633)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/7CTIYcD3WOOf2JRKG_mQ0g-VBkTPlmjVZAl17lebjV9hA)

## Modbus RTU instructions and versions

The [Modbus RTU instructions](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/ud_zuoVlFyzW3~iAWbbOhg?section=X3efdd328fea34a6d9b5bf7851c9138a8) provide the ability to connect to PROFINET and PROFIBUS distributed I/O. They allow you to configure the communications between the PtP communication modules in the distributed I/O rack and the PtP devices. S7‑1200 CM 1241 modules must have a minimum firmware version of V2.1 to use these Modbus RTU instructions. Older S7-1200 CPU programs might use [Legacy Modbus RTU instructions.](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/Z6ES3eY2LA6dewK7N8HPkQ?section=X8c86f98c47e86767b644105918ca1630)

STEP 7 provides different versions of the Modbus RTU instructions. For information on instruction versions, refer to [Use Instruction versions](https://support.industry.siemens.com/cs/ww/en/view/109798671/113722878475) in the STEP 7 Information System.

---

#### Maximum number of supported Modbus slaves

Modbus addressing supports a maximum of 247 slaves (slave numbers 1 through 247). Each Modbus network segment can have a maximum of 32 devices, based upon the loading and drive capabilities of the RS485 interface. When you reach the 32-device limit, you must use a repeater to expand to the next segment. You need seven repeaters to support the 247 slaves connected to one master for RS485.

Siemens repeaters work only with PROFIBUS; their function is to monitor PROFIBUS token passing. You cannot use Siemens repeaters with other protocols. Therefore, you require third party repeaters for Modbus.

Modbus timeouts are long by default; the use of multiple repeaters does not create a time-delay problem. The Modbus master does not care if a slave is slow to respond or if multiple repeaters delay the response.

---

#### Modbus RTU instructions


---

##### Modbus_Comm_Load (Configure SIPLUS I/O or port on the PtP module for Modbus RTU) instruction

Table 1. Modbus\_Comm\_Load instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"Modbus\_Comm\_Load\_DB"(    REQ:=\_bool\_in,    PORT:=\_uint\_in\_,    BAUD:=\_udint\_in\_,    PARITY:=\_uint\_in\_,    FLOW\_CTRL:=\_uint\_in\_,    RTS\_ON\_DLY:=\_uint\_in\_,    RTS\_OFF\_DLY:=\_uint\_in\_,    RESP\_TO:=\_uint\_in\_,    DONE=>\_bool\_out,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    MB\_DB:=\_fbtref\_inout\_);** | The Modbus\_Comm\_Load instruction configures SIPLUS I/O or a PtP port for Modbus RTU protocol communications.  Modbus RTU port hardware options: Install up to three CMs (RS485 or RS232), plus one CB (R4845).  Modbus RTU SIPLUS I/O options: Install ET 200MP S7-1500CM PtP (RS485 / 422 or RS232) or ET 200SP S7-1500 CM PtP (RS485 / 422 or RS232)  An instance data block is assigned automatically when you place the Modbus\_Comm\_Load instruction in your program. |

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| EN | IN | Bool | Note: The Modbus RTU, Modbus\_Comm\_Load instruction uses the RDREC and WRREC instructions to initialize the PTP module. However, the RDREC/WRREC instruction works asynchronously, which means that it takes several scans for the instruction to complete. Therefore, you must hold the EN parameter of the Modbus\_Comm\_Load instruction true until completion of the RDREC/WRREC instruction. |
| REQ | IN | Bool | A low to high (positive edge) signal starts the operation.  (Version 2.0 only) |
| PORT | IN | Port | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. |
| BAUD | IN | UDInt | Baud rate selection:  300, 600, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 76800, 115200, all other values are invalid |
| PARITY | IN | UInt | Parity selection:   - 0 – None - 1 – Odd - 2 – Even |
| FLOW\_CTRL 1 | IN | UInt | Flow control selection:   - 0 – (default) no flow control - 1 – Hardware flow control with RTS always ON (does not apply to RS485 ports) - 2 – Hardware flow control with RTS switched |
| RTS\_ON\_DLY 1 | IN | UInt | RTS ON delay selection:   - 0 – (default) No delay from RTS active until the first character of the message is transmitted - 1 to 65535 – Delay in milliseconds from RTS active until the first character of the message is transmitted (does not apply to RS485 ports). RTS delays shall be applied independent of the FLOW\_CTRL selection. |
| RTS\_OFF\_DLY 1 | IN | UInt | RTS OFF delay selection:   - 0 – (default) No delay from the last character transmitted until RTS goes inactive - 1 to 65535 – Delay in milliseconds from the last character transmitted until RTS goes inactive (does not apply to RS485 ports). RTS delays shall be applied independent of the FLOW\_CTRL selection. |
| RESP\_TO 1 | IN | UInt | Response timeout:  Time in milliseconds allowed by the Modbus\_Master for the slave to respond. If the slave does not respond in this time period, the Modbus\_Master will retry the request or terminate the request with an error when the specified number of retries has been sent.  5 ms to 65535 ms (default value = 1000 ms). |
| MB\_DB | IN | Variant | A reference to the instance data block used by the Modbus\_Master or Modbus\_Slave instructions. After Modbus\_Master or Modbus\_Slave is placed in your program, the DB identifier appears in the parameter helper drop-list available at the MB\_DB box connection. |
| DONE | OUT | Bool | The DONE bit is TRUE for one scan, after the last request was completed with no error. (Version 2.0 only) |
| ERROR | OUT | Bool | The ERROR bit is TRUE for one scan, after the last request was terminated with an error. The error code value at the STATUS parameter is valid only during the single scan where ERROR = TRUE. |
| STATUS | OUT | Word | Execution condition code |

1 Optional parameters for Modbus\_Comm\_Load (V 2.x or later). Click the arrow at the bottom of a LAD/FBD box to expand the box and include these parameters.

Modbus\_Comm\_Load is executed to configure a port for the Modbus RTU protocol. Once a port is configured for the Modbus RTU protocol, it can only be used by either the Modbus\_Master or Modbus\_Slave instructions.

One execution of Modbus\_Comm\_Load must be used to configure each communication port that is used for Modbus communication. Assign a unique Modbus\_Comm\_Load instance DB for each port that you use. You can install up to three communication modules (RS232 or RS485) and one communication board (RS485) in the CPU. Call Modbus\_Comm\_Load from a startup OB and execute it one time or use the [first scan system flag](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/57RJkWqlv2cHgK3TNbVEaA?section=X24485c8cb365163875682d239602aa4b) to initiate the call to execute it one time. Only execute Modbus\_Comm\_Load again if communication parameters like baud rate or parity must change.

If you use the Modbus library with a module in a distributed rack, the Modbus\_Comm\_Load instruction must be executed in a cyclical interrupt routine (for example, once per second or once every 10 seconds). If power is lost to the distributed rack or the module is pulled, upon restoration of module operation, only the HWConfig parameter set is sent to the PtP module. All requests initiated by the Modbus\_Master timeout, and the Modbus\_Slave goes silent (no response to any message). Cyclic execution of the Modbus\_Comm\_Load instruction resolves these issues.

An instance data block is assigned for Modbus\_Master or Modbus\_Slave when you place these instructions in your program. This instance data block is referenced when you specify the MB\_DB parameter for the Modbus\_Comm\_Load instruction.

## Modbus\_Comm\_Load instance data block (DB) tags

The following table shows the public static tags stored in the Modbus\_Comm\_Load instance DB that can be used in your program:

Table 3. Modbus\_Comm\_Load instance DB static tags

| **Tag** | **Data type** | **Default** | **Description** |
| --- | --- | --- | --- |
| ICHAR\_GAP | Word | 0 | Maximum character delay time between characters. This parameter is specified in milliseconds and increases the anticipated period between the received characters. The corresponding number of bit times for this parameter is added to the Modbus default value of 35 bit times (3.5 character times). |
| RETRIES | Word | 2 | Number of retries that the master executes before the error code 0x80C8 for "No response" is returned. |
| EN\_SUPPLY\_VOLT | Bool | 0 | Enable diagnostics for missing supply voltage L+. |
| MODE | USInt | 0 | Operating mode  Valid operating modes are as follows:   - 0 = Full duplex (RS232) - 1 = Full duplex (RS422) four-wire mode (point-to-point) - 2 = Full duplex (RS422) four-wire mode (multipoint master, CM PtP, ET 200SP) - 3 = Full duplex (RS422) four-wire mode (multipoint slave, CM PtP, ET 200SP) - 4 = Half duplex (RS485) two-wire mode (See Note below.) |
| LINE\_PRE | USInt | 0 | Receive line initial state  Valid initial states are as follows:   - 0 = "No" initial state (See Note below.) - 1 = signal R(A) = 5 V DC, signal R(B) = 0 V DC (break detection):  Break detection is possible with this initial state.  Can only be selected with: "Full duplex (RS422) four-wire mode (point-to-point connection)" and "Full duplex (RS422) four-wire mode (multipoint slave)". - 2 = signal R(A) = 0 V DC, signal R(B) = 5 V DC:  This default setting corresponds to the idle state (no active send operation). No break detection is possible with this initial state. |
| BRK\_DET | USInt | 0 | Break detection  The following selections are valid:   - 0 = break detection deactivated - 1 = break detection activated |
| EN\_DIAG\_ALARM | Bool | 0 | Activate diagnostics interrupt:   - 0 = not activated - 1 = activated |
| STOP\_BITS | USInt | 1 | Number of stop bits:   - 1 = 1 stop bit - 2 = 2 stop bits - 0, 3 to 255 = reserved |

Note:

Required setting for the use of PROFIBUS cables with CM 1241 for RS485

Table 4. Modbus\_Comm\_Load execution condition codes 1

| **STATUS (W#16#)** | **Description** |
| --- | --- |
| 0000 | No error |
| 8180 | Invalid port ID value (wrong port/hardware identifier for communication module) |
| 8181 | Invalid baud rate value |
| 8182 | Invalid parity value |
| 8183 | Invalid flow control value |
| 8184 | Invalid response timeout value (response timeout less than the 5 ms minimum) |
| 8185 | MB\_DB parameter is not an instance data block of a Modbus\_Master or Modbus\_Slave instruction. |

1 In addition to the Modbus\_Comm\_Load errors listed above, errors can be returned from the underlying PtP communication instructions.

---

##### Modbus_Master (Communicate using SIPLUS I/O or the PtP port as Modbus RTU master) instruction

Table 1. Modbus\_Master instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"Modbus\_Master\_DB"(    REQ:=\_bool\_in\_,    MB\_ADDR:=\_uint\_in\_,    MODE:=\_usint\_in\_,    DATA\_ADDR:=\_udint\_in\_,    DATA\_LEN:=\_uint\_in\_,    DONE=>\_bool\_out\_,    BUSY=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    DATA\_PTR:=\_variant\_inout\_);** | The Modbus\_Master instruction communicates as a Modbus master using a port that was configured by a previous execution of the Modbus\_Comm\_Load instruction. An instance data block is assigned automatically when you place the Modbus\_Master instruction in your program. This Modbus\_Master instance data block is used when you specify the MB\_DB parameter for the Modbus\_Comm\_Load instruction. |

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | 0=No request  1= Request to transmit data to Modbus slave |
| MB\_ADDR | IN | V1.0: USInt  V2.0: UInt | Modbus RTU station address:  Standard addressing range (1 to 247)  Extended addressing range (1 to 65535)  The value of 0 is reserved for broadcasting a message to all Modbus slaves. Modbus function codes 05, 06, 15 and 16 are the only function codes supported for broadcast. |
| MODE | IN | USInt | Mode Selection: Specifies the type of request (read, write, or diagnostic). See the Modbus functions table below for details. |
| DATA\_ADDR | IN | UDInt | Starting Address in the slave: Specifies the starting address of the data to be accessed in the Modbus slave. See the Modbus functions table below for valid addresses. |
| DATA\_LEN | IN | UInt | Data Length: Specifies the number of bits or words to be accessed in this request. See the Modbus functions table below for valid lengths. |
| DATA\_PTR | IN\_OUT | Variant | Data Pointer: Points to the M or DB address (non-optimized DB type) for the data being written or read. |
| DONE | OUT | Bool | The DONE bit is TRUE for one scan, after the last request was completed with no error. |
| BUSY | OUT | Bool | - 0 – No Modbus\_Master operation in progress - 1 – Modbus\_Master operation in progress |
| ERROR | OUT | Bool | The ERROR bit is TRUE for one scan, after the last request was terminated with an error. The error code value at the STATUS parameter is valid only during the single scan where ERROR = TRUE. |
| STATUS | OUT | Word | Execution condition code |

## Modbus\_Master communication rules

- Modbus\_Comm\_Load must be executed to configure a port before a Modbus\_Master instruction can communicate with that port.
- If a port is to be used to initiate Modbus master requests, that port should not be used by a Modbus\_Slave. One or more instances of Modbus\_Master execution can be used with that port, but all Modbus\_Master execution must use the same Modbus\_Master instance DB for that port.
- The Modbus instructions do not use communication interrupt events to control the communication process. Your program must poll the Modbus\_Master instruction for transmit and receive complete conditions.
- Call all Modbus\_Master execution for a given port from a program cycle OB. Modbus\_Master instructions may execute in only one of the program cycle or cyclic/time delay execution levels. They must not execute in both execution priority levels. Pre-emption of a Modbus\_Master instruction by another Modbus\_Master instruction in a higher priority execution priority level will result in improper operation. Modbus\_Master instructions must not execute in the startup, diagnostic or time error execution priority levels.
- Once a Modbus\_Master instruction initiates a transmission, this instance must be continually executed with the EN input enabled until a DONE=1 state or ERROR=1 state is returned. A particular Modbus\_Master instance is considered active until one of these two events occurs. While the original instance is active, any call to any other instance with the REQ input enabled will result in an error. If the continuous execution of the original instance stops, the request state remains active for a period of time specified by the static variable "Blocked\_Proc\_Timeout". Once this period of time expires, the next Modbus\_Master instruction called with an enabled REQ input will become the active instance. This prevents a single Modbus\_Master instance from monopolizing or locking access to a port. If the original active instance is not enabled within the period of time specified by the static variable "Blocked\_Proc\_Timeout", then the next execution by this instance (with REQ not set) will clear the active state. If (REQ is set), then this execution initiates a new Modbus\_Master request as if no other instance was active.

## REQ parameter

0 = No request; 1 = Request to transmit data to Modbus Slave

You may control this input either through the use of a level or edge triggered contact. Whenever this input is enabled, a state machine is started to ensure that no other Modbus\_Master using the same instance DB is allowed to issue a request, until the current request is completed. All other input states are captured and held internally for the current request, until the response is received or an error detected.

If the same instance of Modbus\_Master is executed again with REQ input = 1 before the completion of the current request, then no subsequent transmissions are made. However, when the request is completed, a new request is issued whenever a Modbus\_Master is executed again with REQ input = 1.

## DATA\_ADDR and MODE parameters select the Modbus function type

DATA\_ADDR (starting Modbus address in the slave): Specifies the starting address of the data to be accessed in the Modbus slave.

The Modbus\_Master instruction uses a MODE input rather than a Function Code input. The combination of MODE and Modbus address determine the Function Code that is used in the actual Modbus message. The following table shows the correspondence between parameter MODE, Modbus function code, and Modbus address range.

Table 3. Modbus functions

| **MODE** | **Modbus function** | **Data length** | **Operation and data** | **Modbus address** |
| --- | --- | --- | --- | --- |
| 0 | 01 | 1 to 2000  1 to 1992 1 | Read output bits:  1 to (1992 or 2000) bits per request | 1 to 9999 |
| 0 | 02 | 1 to 2000  1 to 1992 1 | Read input bits:  1 to (1992 or 2000) bits per request | 10001 to 19999 |
| 0 | 03 | 1 to 125  1 to 124 1 | Read Holding registers:  1 to (124 or 125) words per request | 40001 to 49999 or  400001 to 465535 |
| 0 | 04 | 1 to 125  1 to 124 1 | Read input words:  1 to (124 or 125) words per request | 30001 to 39999 |
| 104 | 04 | 1 to 125  1 to 124 1 | Read input words:  1 to (124 or 125) words per request | 00000 to 65535 |
| 1 | 05 | 1 | Write one output bit:  One bit per request | 1 to 9999 |
| 1 | 06 | 1 | Write one holding register:  1 word per request | 40001 to 49999 or  400001 to 465535 |
| 1 | 15 | 2 to 1968  2 to 1960 1 | Write multiple output bits:  2 to (1960 or 1968) bits per request | 1 to 9999 |
| 1 | 16 | 2 to 123  2 to 122 1 | Write multiple holding registers:  2 to (122 or 123) words per request | 40001 to 49999 or  400001 to 465535 |
| 2 | 15 | 1 to 1968  2 to 1960 1 | Write one or more output bits:  1 to (1960 or 1968) bits per request | 1 to 9999 |
| 2 | 16 | 1 to 123  1 to 122 1 | Write one or more holding registers:  1 to (122 or 123) words per request | 40001 to 49999 or  400001 to 465535 |
| 11 | 11 | 0 | Read the slave communication status word and event counter. The status word indicates busy (0 – not busy, 0xFFFF - busy). The event counter is incremented for each successful completion of a message.  Both the DATA\_ADDR and DATA\_LEN operands of the Modbus\_Master instruction are ignored for this function. |  |
| 80 | 08 | 1 | Check slave status using data diagnostic code 0x0000 (Loopback test – slave echoes the request)  1 word per request |  |
| 81 | 08 | 1 | Reset slave event counter using data diagnostic code 0x000A  1 word per request |  |
| 3 to 10,  12 to 79,  82 to 255 |  |  | Reserved |  |

1For "Extended Addressing" mode the maximum data lengths are reduced by 1 byte or 1 word depending upon the data type used by the function.

## DATA\_PTR parameter

The DATA\_PTR parameter points to the DB or M address that is written to or read from. If you use a data block, then you must create a global data block that provides data storage for reads and writes to Modbus slaves.

Note:

**The DATA\_PTR data block type must allow direct addressing**

The data block must allow both direct (absolute) and symbolic addressing. When you create the data block the "Standard" access attribute must be selected.

As of Modbus\_Master instruction version V4.0 or later, you can enable the data block attribute "Optimized block access". You can only use a single element, or an array of elements, in optimized memory with the following data types: Bool, Byte, Char, Word, Int, DWord, Dint, Real, USInt, UInt, UDInt, SInt, or WChar.

## Data block structures for the DATA\_PTR parameter

- These data types are valid for **word reads** of Modbus addresses 30001 to 39999, 40001 to 49999, and 400001 to 465536 and also for **word writes** to Modbus addresses 40001 to 49999 and 400001 to 465536.

  - Standard array of WORD, UINT, or INT data types
  - Named WORD, UINT, or INT structure where each element has a unique name and 16 bit data type.
  - Named complex structure where each element has a unique name and a 16 or 32 bit data type.
- For **bit reads** and writes of Modbus addresses 00001 to 09999 and bit reads of 10001 to 19999.

  - Standard array of Boolean data types.
  - Named Boolean structure of uniquely named Boolean variables.
- Although not required, it is recommended that each Modbus\_Master instruction have its own separate memory area. The reason for this recommendation is that there is a greater possibility of data corruption if multiple Modbus\_Master instructions are reading and writing to the same memory area.
- There is no requirement that the DATA\_PTR data areas be in the same global data block. You can create one data block with multiple areas for Modbus reads, one data block for Modbus writes, or one data block for each slave station.

## Modbus\_Master instruction data block (DB) variables

The following table shows the public static tags stored in the Modbus\_Master instance DB that you can use in your program:

Table 4. Modbus\_Master instance DB static variables

| **Tag** | **Data type** | **Default** | **Description** |
| --- | --- | --- | --- |
| Blocked\_Proc\_Timeout | Real | 3.0 | Duration (in seconds) for which to wait for a blocked Modbus\_Master instance before this instance is removed as ACTIVE. This can occur, for example, if a Modbus\_Master request is issued and the program then stops to call the Modbus\_Master function before it has completely finished the request. The time value must be greater than 0 and less than 55 seconds, or an error occurs. |
| Extended\_Addressing | Bool | FALSE | Configures single or double-byte slave station addressing:   - FALSE = One-byte address; 0 to 247 - TRUE = Two-byte address (corresponds to extended addressing); 0 to 65535 |
| MB\_DB | MB\_BASE | - | The MB\_DB parameter of the Modbus\_Comm\_Load instruction must be connected to the MB\_DB parameter of the Modbus\_Master instruction. |

Your program can write values to the Blocked\_Proc\_Timeout and Extended\_Addressing variables to control the Modbus\_Master operations. See the Modbus\_Slave topic description of [HR\_Start\_Offset](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/tw2aGuN3pgXgOSYXiTpBUQ?section=Xebe38539f560d10040816e4f68570d04) and [Extended\_Addressing](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/tw2aGuN3pgXgOSYXiTpBUQ?section=Xebe38539f560d10040816e4f68570d04) for an example of how to use these variables in the program editor and details about Modbus extended addressing.

## Condition codes

Table 5. Modbus\_Master execution condition codes (communication and configuration errors) 1

| **STATUS (W#16#)** | **Description** |
| --- | --- |
| 0000 | No error |
| 80C8 | Slave timeout. The specified slave did not respond in the specified time. Please check the baud rate, parity, and wiring of the slave device. This error is only reported after any configured retries have been attempted. |
| 80C9 | The Modbus\_Master instruction has timed out for one of the following reasons:   - The instruction is waiting for a response from the module that is being used for communications. - The Blocked\_Proc\_Timeout value is set too small.   This error is reported if a PROFIBUS or PROFINET distributed I/O device returns from one of the following:   - An interruption to power or communication - A communication module pull/plug event   In these instances, the hardware configuration from the PLC is reloaded, and Modbus\_Comm\_Load must be executed again to properly configure the communication module. |
| 80D1 | The receiver issued a flow control request to suspend an active transmission and never re-enabled the transmission during the specified wait time.  This error is also generated during hardware flow control when the receiver does not assert CTS within the specified wait time. |
| 80D2 | The transmit request was aborted because no DSR signal is received from the DCE. |
| 80E0 | The message was terminated because the receive buffer is full. |
| 80E1 | The message was terminated as a result of a parity error. |
| 80E2 | The message was terminated as a result of a framing error. |
| 80E3 | The message was terminated as a result of an overrun error. |
| 80E4 | The message was terminated as a result of the specified length exceeding the total buffer size. |
| 8180 | Invalid port ID value or error with Modbus\_Comm\_Load instruction |
| 8186 | Invalid Modbus station address |
| 8188 | Invalid Mode specified for broadcast request |
| 8189 | Invalid Data Address value |
| 818A | Invalid Data Length value |
| 818B | Invalid pointer to the local data source/destination: Size not correct |
| 818C | Invalid pointer for DATA\_PTR or invalid Blocked\_Proc\_Timeout. The data area must be one of the following:   - Classic DB - Array of elemental data types in a symbolic or retentive DB - M memory |
| 8200 | Port is busy processing a transmit request. |
| 8280 | Negative acknowledgement when reading module. Check the input at the PORT parameter. This can be caused by the loss of a PROFIBUS or PROFINET distributed I/O module, either by a station power or communication loss or a module pull. |
| 8281 | Negative acknowledgement when writing to module. Check the input at the PORT parameter. This can be caused by the loss of a PROFIBUS or PROFINET distributed I/O module, either by a station power or communication loss or a module pull. |

Table 6. Modbus\_Master execution condition codes (Modbus protocol errors) 1

| **STATUS (W#16#)** | **Response code from slave** | **Modbus protocol errors** |
| --- | --- | --- |
| 8380 | - | CRC error |
| 8381 | 01 | Function code not supported |
| 8382 | 03 | Data length error |
| 8383 | 02 | Data address error or address outside the valid range of the DATA\_PTR area |
| 8384 | Greater than 03 | Data value error |
| 8385 | 03 | Data diagnostic code value not supported (function code 08) |
| 8386 | - | Function code in the response does not match the code in the request. |
| 8387 | - | Wrong slave responded |
| 8388 | - | The slave response to a write request is incorrect. The write request returned by the slave does not match what the master actually sent. |

1 In addition to the Modbus\_Master errors listed above, errors can be returned from the underlying PtP communication instructions.

Note:

**Setting the maximum record length for Profibus communication**

When using a CM1243-5 Profibus Master module to control an ET 200SP or ET 200MP Profibus device that uses an RS232, RS422, or RS485 point-to-point module, you need to explicitly set the "max\_record\_len" data block tag to 240 as defined below:

Set "max\_record\_len" in the Send\_P2P section of the instance DB (for example, "Modbus\_Master\_DB".Send\_P2P.max\_record\_len) to 240 after running Modbus\_Comm\_Load.

Explicitly assigning max\_record\_len is only necessary with Profibus communication; Profinet communication already uses a valid max\_record\_len value.

---

##### Modbus_Slave (Communicate using SIPLUS I/O or the PtP port as Modbus RTU slave) instruction

Table 1. Modbus\_Slave instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"Modbus\_Slave\_DB"(    MB\_ADDR:=\_uint\_in\_,    NDR=>\_bool\_out\_,    DR=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    MB\_HOLD\_REG:=\_variant\_inout\_);** | The Modbus\_Slave instruction allows your program to communicate in one of two ways:   - As a Modbus RTU slave through a PtP port on the CM (RS485 or RS232) and CB (RS485) - As a Modbus RTU slave through Modbus RTU SIPLUS I/O options:    - Install ET 200MP S7-1500CM PtP (RS485 / 422 or RS232).   - Install ET 200SP S7-1500 CM PtP (RS485 / 422 or RS232).   When a remote Modbus RTU master issues a request, your user program responds to the request by Modbus\_Slave execution. STEP 7 automatically creates an instance DB when you insert the instruction. Use this Modbus\_Slave\_DB name when you specify the MB\_DB parameter for the Modbus\_Comm\_Load instruction. |

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| MB\_ADDR | IN | V1.0: USInt  V2.0: UInt | The station address of the Modbus slave:  Standard addressing range (1 to 247)  Extended addressing range (0 to 65535) |
| MB\_HOLD\_REG | IN\_OUT | Variant | Pointer to the Modbus Holding Register DB: The Modbus holding register can be M memory or a data block. |
| NDR | OUT | Bool | New Data Ready:   - 0 – No new data - 1 – Indicates that new data has been written by the Modbus master |
| DR | OUT | Bool | Data Read:   - 0 – No data read - 1 – Indicates that data has been read by the Modbus master |
| ERROR | OUT | Bool | The ERROR bit is TRUE for one scan, after the last request was terminated with an error. If execution is terminated with an error, then the error code value at the STATUS parameter is valid only during the single scan where ERROR = TRUE. |
| STATUS | OUT | Word | Execution error code |

Modbus communication function codes (1, 2, 4, 5, and 15) can read and write bits and words directly in the input process image and output process image of the CPU. For these function codes, the MB\_HOLD\_REG parameter must be defined as a data type larger than a byte. The following table shows the example mapping of Modbus addresses to the process image in the CPU.

Table 3. Mapping of Modbus addresses to the process image

| **Modbus functions** | | | | | | **S7-1200** | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Codes | Function | Data area | Address range | | | Data area | CPU address |
| 01 | Read bits | Output | 1 | to | 8192 | Output Process Image | Q0.0 to Q1023.7 |
| 02 | Read bits | Input | 10001 | to | 18192 | Input Process Image | I0.0 to I1023.7 |
| 04 | Read words | Input | 30001 | to | 30512 | Input Process Image | IW0 to IW1022 |
| 05 | Write bit | Output | 1 | to | 8192 | Output Process Image | Q0.0 to Q1023.7 |
| 15 | Write bits | Output | 1 | to | 8192 | Output Process Image | Q0.0 to Q1023.7 |

Modbus communication function codes (3, 6, 16) use a Modbus holding register which can be an M memory address range or a data block. The type of holding register is specified by the MB\_HOLD\_REG parameter on the Modbus\_Slave instruction.

Note:

**MB\_HOLD\_REG data block type**

A Modbus holding register data block must allow both direct (absolute) and symbolic addressing. When you create the data block the "Standard" access attribute must be selected.

As of Modbus\_Slave instruction version V4.0 or later, you can enable the data block attribute "Optimized block access". You can only use a single element, or an array of elements, in optimized memory with the following data types: Bool, Byte, Char, Word, Int, DWord, Dint, Real, USInt, UInt, UDInt, SInt, or WChar.

The following table shows examples of Modbus address to holding register mapping that is used for Modbus function codes 03 (read words), 06 (write word), and 16 (write words). The actual upper limit of DB addresses is determined by the maximum work memory limit and M memory limit, for each CPU model.

Table 4. Mapping of Modbus addresses to CPU memory

| **Modbus master address** | **MB\_HOLD\_REG parameter examples** | | | | |
| --- | --- | --- | --- | --- | --- |
| **MW100** | **DB10.DBw0** | **MW120** | **DB10.DBW50** | **"Recipe".ingredient** |
| 40001 | MW100 | DB10.DBW0 | MW120 | DB10.DBW50 | "Recipe".ingredient[1] |
| 40002 | MW102 | DB10.DBW2 | MW122 | DB10.DBW52 | "Recipe".ingredient[2] |
| 40003 | MW104 | DB10.DBW4 | MW124 | DB10.DBW54 | "Recipe".ingredient[3] |
| 40004 | MW106 | DB10.DBW6 | MW126 | DB10.DBW56 | "Recipe".ingredient[4] |
| 40005 | MW108 | DB10.DBW8 | MW128 | DB10.DBW58 | "Recipe".ingredient[5] |

Table 5. Diagnostic functions

| **S7-1200 Modbus\_Slave Modbus diagnostic functions** | | |
| --- | --- | --- |
| Codes | Sub-function | Description |
| 08 | 0000H | Return query data echo test:   - Prior to STEP 7 V15.1, the Modbus\_Slave echos back to a Modbus master a word of data that is received. - As of STEP 7 V15.1 or later, the Modbus\_Slave instruction V4.1 or later echos back one or more words of data that is received. |
| 08 | 000AH | Clear communication event counter: The Modbus\_Slave will clear out the communication event counter that is used for Modbus function 11. |
| 11 |  | Get communication event counter: The Modbus\_Slave uses an internal communication event counter for recording the number of successful Modbus read and write requests that are sent to the Modbus\_Slave. The counter does not increment on any Function 8, Function 11, or broadcast requests. It is also not incremented on any requests that result in a communication error (for example, parity or CRC errors). |

The Modbus\_Slave instruction supports broadcast write requests from any Modbus master as long as the request is for accessing valid addresses. Modbus\_Slave will produce error code "0x8188" for function codes not supported in broadcast.

## Modbus\_Slave communication rules

- Modbus\_Comm\_Load must be executed to configure a port, before a Modbus\_Slave instruction can communicate through that port.
- If a port is to respond as a slave to a Modbus\_Master, then do not program that port with the Modbus\_Master instruction.
- Only one instance of Modbus\_Slave can be used with a given port, otherwise erratic behavior may occur.
- The Modbus instructions do not use communication interrupt events to control the communication process. Your program must control the communication process by polling the Modbus\_Slave instruction for transmit and receive complete conditions.
- The Modbus\_Slaveinstruction must execute periodically at a rate that allows it to make a timely response to incoming requests from a Modbus\_Master. It is recommended that you execute Modbus\_Slave every scan from a program cycle OB. Executing Modbus\_Slave from a cyclic interrupt OB is possible, but is not recommended because of the potential for excessive time delays in the interrupt routine to temporarily block the execution of other interrupt routines.

## Modbus signal timing

Modbus\_Slave must be executed periodically to receive each request from the Modbus\_Master and then respond as required. The frequency of execution for Modbus\_Slave is dependent upon the response timeout period of the Modbus\_Master. This is illustrated in the following diagram.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/EOiTFxYH2x0ndWDRRXpI2g-VBkTPlmjVZAl17lebjV9hA/resized-content?v=19ddf7326e33f793)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/EOiTFxYH2x0ndWDRRXpI2g-VBkTPlmjVZAl17lebjV9hA)

The response timeout period RESP\_TO is the amount of time a Modbus\_Master waits for the start of a response from a Modbus\_Slave. This time period is not defined by the Modbus protocol, but is a parameter of each Modbus\_Master. The frequency of execution (the time between one execution and the next execution) of Modbus\_Slave must be based upon the particular parameters of your Modbus\_Master. At a minimum, you should execute Modbus\_Slave twice within the response timeout period of the Modbus\_Master.

## Modbus\_Slave instruction data block (DB) variables

The following table shows the public static tags stored in the Modbus\_Slave instance DB that you can use in your program:

Table 6. Modbus\_Slave instance DB static variables

| **Variable** | **Data type** | **Default** | **Description** |
| --- | --- | --- | --- |
| HR\_Start\_Offset | Word | 0 | Assigns the starting address of the Modbus holding register (default = 0) |
| Extended\_Addressing | Bool | FALSE | Configures single or double-byte slave addressing:   - FALSE = single byte address - TRUE = double-byte address |
| Request\_Count | Word | 0 | Total of all requests received by this slave |
| Slave\_Message\_Count | Word | 0 | Number of requests received for this specific slave |
| Bad\_CRC\_Count | Word | 0 | Number of requests received that have a CRC error |
| Broadcast\_Count | Word | 0 | Number of broadcast requests received |
| Exception\_Count | Word | 0 | Modbus-specific errors that require an acknowledgement with a returned exception to the master |
| Success\_Count | Word | 0 | Number of requests received for this specific slave that have no protocol errors |
| MB\_DB | MB\_BASE | - | The MB\_DB parameter of the Modbus\_Comm\_Load instruction must be connected to the MB\_DB parameter of the Modbus\_Slave instruction. |
| QB\_Start | UInt | 0 | The starting address of the output bytes to which the CPU can write (QB0 to QB65535) |
| QB\_Count | UInt | 65535 | The number of bytes to which a remote device can write. If QB\_Count = 0, a remote device cannot write to the outputs.  Example: To allow only QB10 through QB17 to be writable, QB\_Start = 10 and QB\_Count = 8. |
| QB\_Read\_Start | UInt | 0 | The starting address of the output bytes to which the CPU can read (QB0 to QB65535) |
| QB\_Read\_Count | UInt | 65535 | The number of output bytes from which a remote device can read. If QB\_Count = 0, a remote device cannot read from the outputs. Example: To allow only QB10 through QB17 to be readable, QB\_Start = 10 and QB\_Count = 8. |
| IB\_Read\_Start | UInt | 0 | The starting address of the input bytes to which the CPU can read (IB0 to IB65535) |
| IB\_Read\_Count | UInt | 65535 | The number of input bytes from which a remote device can read. If IB\_Count = 0, a remote device cannot read from the inputs. Example: To allow only IB10 through IB17 to be readable, IB\_Start = 10 and IB\_Count = 8. |

Your program can write data to the control Modbus server operations and the following variables:

- HR\_Start\_Offset
- Extended\_Addressing
- QB\_Start
- QB\_Count
- QB\_Read\_Start
- QB\_Read\_Count
- IB\_Read\_Start
- IB\_Read\_Count

Version requirements for Modbus\_Slave instruction data block (DB) variables availability are as follows:

Table 7. Modbus\_Slave instruction data block (DB) variables availability version requirements: Instruction, TIA Portal, and S7‑1200 CPU

| **Modbus\_Slave instruction version** | **TIA Portal version** | **S7-1200 CPU firmware (FW) version** | **Data block variables** |
| --- | --- | --- | --- |
| 3.0 | V14 SP1 | CPU FW V4.0 or later | QB\_Start |
| QB\_Count |
| 4.0 or later | V15 or later | CPU FW V4.2 or later | QB\_Start |
| QB\_Count |
| QB\_Read\_Start |
| QB\_Read\_Count |
| IB\_Read\_Start |
| IB\_Read\_Count |

## HR\_Start\_Offset

Modbus holding register addresses begin at 40001 or 400001. These addresses correspond to the beginning PLC memory address of the holding register. However, you can configure the "HR\_Start\_Offset" variable to start the beginning Modbus holding register address at another value instead of 40001 or 400001.

For example, if the holding register is configured to start at MW100 and is 100 words long. An offset of 20 specifies a beginning holding register address of 40021 instead of 40001. Any address below 40021 and above 400119 will result in an addressing error.

Table 8. Example of Modbus holding register addressing

| **HR\_Start\_Offset** | **Address** | **Minimum** | **Maximum** |
| --- | --- | --- | --- |
| 0 | Modbus address (Word) | 40001 | 40099 |
| S7-1200 address | MW100 | MW298 |
| 20 | Modbus address (Word) | 40021 | 40119 |
| S7-1200 address | MW100 | MW298 |

HR\_Start\_Offset is a word value that specifies the starting address of the Modbus holding register and is stored in the Modbus\_Slave instance data block. You can set this public static variable value by using the parameter helper drop-list, after Modbus\_Slave is placed in your program.

For example, after Modbus\_Slave is placed in a LAD network, you can go to a previous network and assign the HR\_Start\_Offset value. The value must be assigned prior to execution of Modbus\_Slave.

|  |  |
| --- | --- |
|  | Entering a Modbus slave variable using the default DB name:   1. Set the cursor in the parameter field and type an m character. 2. Select "Modbus\_Slave\_DB" from the drop-list. 3. Set the cursor at the right side of the DB name (after the quote character) and enter a period character. 4. Select "Modbus\_Slave\_DB.HR\_Start\_Offset" from the drop list. |
|  |
|  |

## Extended\_Addressing

The Extended\_Addressing variable is accessed in a similar way as the HR\_Start\_Offset reference discussed above except that the Extended\_Addressing variable is a Boolean value. The Boolean value must be written by an output coil and not a move box.

Modbus slave addressing can be configured to be either a single byte (which is the Modbus standard) or double byte. Extended addressing is used to address more than 247 devices within a single network. Selecting extended addressing allows you to address a maximum of 64000 addresses. A Modbus function 1 frame is shown below as an example.

Table 9. Single-byte slave address (byte 0)

| **Function 1** | **Byte 0** | **Byte 1** | **Byte 2** | **Byte 3** | **Byte 4** | **Byte 5** |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Request | Slave addr. | F code | Start address | | Length of coils | |  |
| Valid Response | Slave addr. | F code | Length | Coil data | | |  |
| Error response | Slave addr. | 0x81 | E code |  |  |  |  |

Table 10. Double-byte slave address (byte 0 and byte 1)

|  | **Byte 0** | **Byte 1** | **Byte 2** | **Byte 3** | **Byte 4** | **Byte 5** | **Byte 6** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Request | Slave address | | F code | Start address | | Length of coils | |
| Valid Response | Slave address | | F code | Length | Coil data | | |
| Error response | Slave address | | 0x81 | E code |  |  |  |

## Access to data areas in data blocks (DB) instead of direct access to Modbus addresses

You can access data areas in DBs in the global DB "Attributes" Property page. You must deselect the "Only store in load memory" and "Optimized block access" check boxes.

If a Modbus request arrives and you did not define a data area for the Modbus data type of the corresponding function code, the Modbus\_Slave instruction treats the request as in previous instruction versions: You access process images and holding registers directly.

If you have defined a data area for the Modbus data type of the function code, the Modbus\_Slave instruction reads from or writes to that data area. Whether it reads or writes depends on the job type.

Note:

If a data area is configured, the Modbus\_Slave instruction ignores the offsets or ranges configured by the static variables in the instance data block that corresponds to the data\_type of the data area. Those offsets and ranges only apply to the process image or the memory referenced by MB\_HOLD\_REG. The data area start and length parameters provide its own way of defining offsets and ranges

For one individual Modbus request, you can only read from or write to one data area. If, for example, you want to read holding registers that extend over multiple data areas, you require multiple Modbus requests.

These are the rules for defining data areas:

- You can define up to eight data areas in different DBs; each DB must only contain one data area. An individual MODBUS request can only read from precisely one data area or write to precisely one data area. Each data area corresponds to one MODBUS address area. You define the data areas in the "Data\_Area\_Array" static tag of the instance DB.
- If you want to use less than eight data areas, you must place the required data areas one behind the other, without any gaps. The first blank entry in the data areas ends the data area search during processing. If, for example, you define the field elements 1, 2, 4, and 5, the "Data\_Area\_Array" only recognizes field elements 1 and 2. as field element 3 is empty.
- The Data\_Area\_Array field consists of eight elements: Data\_Area\_Array[1] to Data\_Area\_Array[8]
- Each field element Data\_Area\_Array[x], 1 <= x <= 8, is a UDT of the type MB\_DataArea and is structured as follows:

  | **Parameter** | **Data type** | **Meaning** |
  | --- | --- | --- |
  | data\_ type | UInt | Identifier for the MODBUS data type that is mapped to this data area:  - 0: Identifier for an empty field element or an unused data area. In this case, the values of db, start and length are irrelevant. - 1: Process image output (used with function codes 1, 5, and 15) - 2: Process image input (used with function code 2) - 3: Holding register (used with function codes 3, 6, and 16) - 4: Input register (used with function code 4) Note: If you have defined a data area for a MODBUS data type, the instruction Modbus\_Slave can no longer access this MODBUS data type directly. If the address of a MODBUS request for such a data type does not correspond to a defined data area, a value of W#16#8383 is returned in STATUS. |
  | db | UInt | Number of the data block to which the MODBUS register or bits subsequently defined are mapped  The DB number must be unique in the data areas. The same DB number must not be defined in multiple data areas.  In the global DB "Attributes" Property page, you must deselect the "Only store in load memory" and "Optimized block access" check boxes.  Data areas also start with the byte address 0 of the DB.  Permitted values: 1 to 60999 |
  | start | UInt | First MODBUS address that is mapped to the data block starting from address 0.0  Permitted values: 0 to 65535 |
  | length | UInt | Number of bits (for the values 1 and 2 of data\_type) or number of registers (for the values 3 and 4 of data\_type)  The MODBUS address areas of one and the same MODBUS data type must not overlap.  Permitted values: 1 to 65535 |

Examples of the definition of data areas:

- First example: data\_type = 3, db = 1, start = 10, length = 6

  The CPU maps the holding registers (data\_type = 3) in data block 1 (db = 1), placing the Modbus address 10 (start = 10) at data word 0 and the last valid Modbus address 15 (length = 6) at data word 5.
- Second example: data\_type = 2, db = 15, start = 1700, length = 112

  The CPU maps the inputs (data\_type = 2) in data block 15 (db = 15), placing the Modbus address 1700 (start = 1700) at data word 0 and the last valid Modbus address 1811 (length = 112) at data word 111.

## Condition codes

Table 11. Modbus\_Slave execution condition codes (communication and configuration errors) 1

| **STATUS (W#16#)** | **Description** |
| --- | --- |
| 80D1 | The receiver issued a flow control request to suspend an active transmission and never re-enabled the transmission during the specified wait time.  This error is also generated during hardware flow control when the receiver does not assert CTS within the specified wait time. |
| 80D2 | The transmit request was aborted because no DSR signal is received from the DCE. |
| 80E0 | The message was terminated because the receive buffer is full. |
| 80E1 | The message was terminated as a result of a parity error. |
| 80E2 | The message was terminated as a result of a framing error. |
| 80E3 | The message was terminated as a result of an overrun error. |
| 80E4 | The message was terminated as a result of the specified length exceeding the total buffer size. |
| 8180 | Invalid port ID value or error with Modbus\_Comm\_Load instruction |
| 8186 | Invalid Modbus station address |
| 8187 | Invalid pointer to MB\_HOLD\_REG DB: Area is too small |
| 818C | Invalid MB\_HOLD\_REG pointer. The data area must be one of the following:   - Classic DB - Array of elemental data types in a symbolic or retentive DB - M memory |

Table 12. Modbus\_Slave execution condition codes (Modbus protocol errors) 1

| **STATUS (W#16#)** | **Response code from slave** | **Modbus protocol errors** |
| --- | --- | --- |
| 8380 | No response | CRC error |
| 8381 | 01 | Function code not supported or not supported within broadcasts |
| 8382 | 03 | Data length error |
| 8383 | 02 | Data address error or address outside the valid range of the DATA\_PTR area |
| 8384 | 03 | Data value error |
| 8385 | 03 | Data diagnostic code value not supported (function code 08) |
| 8389 |  | Invalid data area definition:   - Invalid data\_type value - DB number invalid or does not exist:    - Invalid db value   - DB number does not exist   - DB number is already used by another data area   - DB with optimized access   - DB is not located in the work memory - Invalid length value - Overlapping of MODBUS address ranges that belong to the same MODBUS data type |

1 In addition to the Modbus\_Slave errors listed above, errors can be returned from the underlying PtP communication instructions.

Note:

**Setting the maximum record length for PROFIBUS communication**

When using a CM1243-5 PROFIBUS Master module to control an ET 200SP or ET 200MP PROFIBUS device that uses an RS232, RS422, or RS485 point-to-point module, you need to explicitly set the "max\_record\_len" data block tag to 240 as defined below:

Set "max\_record\_len" in the Send\_P2P section of the instance DB (for example, "Modbus\_Slave\_DB".Send\_P2P.max\_record\_len) to 240 after running Modbus\_Comm\_Load.

Explicitly assigning max\_record\_len is only necessary with PROFIBUS communication; PROFINET communication already uses a valid max\_record\_len value.

---

#### Modbus RTU examples


---

##### Example: Modbus RTU master program

Modbus\_Comm\_Load is initialized during start-up by using the first scan flag. Execution of Modbus\_Comm\_Load in this manner should only be done when the serial port configuration will not change at runtime.

**Network 1**: Configure/initialize the RS485 module communications port only once during the first scan.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/1_LQTSePZ_GNuswFza0oNA-VBkTPlmjVZAl17lebjV9hA/content?v=ccbeeb1d3fc109ea)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/1_LQTSePZ_GNuswFza0oNA-VBkTPlmjVZAl17lebjV9hA)

One Modbus\_Master instruction is used in the program cycle OB to communicate with a single slave. Additional Modbus\_Master instructions can be used in the program cycle OB to communicate with other slaves, or one Modbus\_Master FB could be re-used to communicate with additional slaves.

**Network 2**: Read 100 words of holding register data from location 400001 on slave #2 to memory location MW500-MW698.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/J3dS~~cywmxmowUajeBNAw-VBkTPlmjVZAl17lebjV9hA/content?v=c10f4961b79ce8f1)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/J3dS~~cywmxmowUajeBNAw-VBkTPlmjVZAl17lebjV9hA)

**Network 3**: Move the first 3 words of the holding register data that has been read to some other location, and set a DONE history bit. This network also sets an ERROR history bit and saves the STATUS word to another location in the event of an error.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/AetcW_ZfP~rhS~kWI057cg-VBkTPlmjVZAl17lebjV9hA/content?v=aed871db6183d412)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/AetcW_ZfP~rhS~kWI057cg-VBkTPlmjVZAl17lebjV9hA)

**Network 4**: Write 64 bits of data from MW600-MW607 to output bit locations 00017 to 00081 on slave #2.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/XIXcYD5oYsmO0HPHA44p0Q-VBkTPlmjVZAl17lebjV9hA/content?v=f20680bd55177dc7)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/XIXcYD5oYsmO0HPHA44p0Q-VBkTPlmjVZAl17lebjV9hA)

**Network 5**: Set a DONE history bit when the write is complete. If an error occurs, the program sets an ERROR history bit and saves the STATUS code.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/FmA5yG7jhx0Ys2hH2LnUrg-VBkTPlmjVZAl17lebjV9hA/content?v=9693fb8d1814cc0d)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/FmA5yG7jhx0Ys2hH2LnUrg-VBkTPlmjVZAl17lebjV9hA)

---

##### Example: Modbus RTU slave program

MB\_COMM\_LOAD shown below is initialized each time "Tag\_1" is enabled.

Execution of MB\_COMM\_LOAD in this manner should only be done when the serial port configuration will change at runtime, as a result of HMI configuration.

**Network 1**: Initialize the RS485 module parameters each time they are changed by an HMI device.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/YeUjFYs9vlPyI1iBei5bng-VBkTPlmjVZAl17lebjV9hA/content?v=be48de5db8b5a034)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/YeUjFYs9vlPyI1iBei5bng-VBkTPlmjVZAl17lebjV9hA)

MB\_SLAVE shown below is placed in a cyclic OB that is executed every 10 ms. While this does not give the absolute fastest response by the slave, it does provide good performance at 9600 baud for short messages (20 bytes or less in the request).

**Network 2**: Check for Modbus master requests during each scan. The Modbus holding register is configured for 100 words starting at MW1000.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/~dq3hvYwpLa9BxL8fKm3Bg-VBkTPlmjVZAl17lebjV9hA/resized-content?v=1141aafd91f64590)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/~dq3hvYwpLa9BxL8fKm3Bg-VBkTPlmjVZAl17lebjV9hA)

---

## Legacy PtP communication (CM/CB 1241 only)


---

### Overview - legacy PtP communication instructions

Prior to the release of STEP 7 V13 SP1 and the S7-1200 V4.1 CPUs, the point-to-point communication instructions existed with different names, and in some cases, slightly different interfaces. The general concepts about [point-to-point communication](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/AVZzqDzfbhog4Raw27Wzbw?section=Xa917f049f16e4d114029a2eef39a3b06), as well as [port](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/z0n0zJNqfqu5cQjfXFOiUA?section=X22d93711fb0b0fbaa1e90e3d9c63f250) and [parameter configuration](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/stMdI~i5k1wrAf398GR3AA?section=X03af0d734df93e2cc6a84931ce873f8e) apply to both sets of instructions. Refer to the individual legacy point-to-point instructions for programming information.

---

### Legacy condition codes

Table 1. Common error classes

| **Class description** | **Error classes** | **Description** |
| --- | --- | --- |
| Port configuration | 80Ax | Used to define common port configuration errors |
| Transmit configuration | 80Bx | Used to define common transmit configuration errors |
| Receive configuration | 80Cx | Used to define common receive configuration errors |
| Transmission runtime | 80Dx | Used to define common transmission runtime errors |
| Reception runtime | 80Ex | Used to define common reception runtime errors |
| Signal handling | 80Fx | Used to define common errors associated with all signal handling |

---

### Legacy point-to-point instructions


---

#### PORT_CFG (Configure communication parameters dynamically)

Table 1. PORT\_CFG (Port Configuration) instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"PORT\_CFG\_DB"(    REQ:=\_bool\_in\_,    PORT:=\_uint\_in\_,    PROTOCOL:=\_uint\_in\_,    BAUD:=\_uint\_in\_,    PARITY:=\_uint\_in\_,    DATABITS:=\_uint\_in\_,    STOPBITS:=\_uint\_in\_,    FLOWCTRL:=\_uint\_in\_,    XONCHAR:=\_char\_in\_,    XOFFCHAR:=\_char\_in\_,    WAITTIME:=\_uint\_in\_,    DONE=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_);** | PORT\_CFG allows you to change port parameters such as baud rate from your program.  You can set up the initial static configuration of the port in the device configuration properties, or just use the default values. You can execute the PORT\_CFG instruction in your program to change the configuration. |

1 STEP 7 automatically creates the DB when you insert the instruction.

The PORT\_CFG configuration changes are not permanently stored in the CPU. The parameters configured in the device configuration are restored when the CPU transitions from RUN to STOP mode and after a power cycle. See [Configuring the communication ports](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/z0n0zJNqfqu5cQjfXFOiUA?section=X22d93711fb0b0fbaa1e90e3d9c63f250) and [Managing flow control](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/vO3D9h3~6H1cp2AQl8IxsA?section=X42fd8bcd964541c16277f0a79c4ebf49) for more information.

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Activate the configuration change on rising edge of this input. (Default value: False) |
| PORT | IN | PORT | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. (Default value: 0) |
| PROTOCOL | IN | UInt | 0 - Point-to-Point communication protocol (Default value)  1..n - future definition for specific protocols |
| BAUD | IN | UInt | Port baud rate (Default value: 6):  1 = 300 baud, 2 = 600 baud, 3 = 1200 baud, 4 = 2400 baud, 5 = 4800 baud, 6 = 9600 baud, 7 = 19200 baud, 8 = 38400 baud, 9 = 57600 baud, 10 = 76800 baud, 11 = 115200 baud |
| PARITY | IN | UInt | Port parity (Default value: 1):  1 = No parity, 2 = Even parity, 3 = Odd parity, 4 = Mark parity, 5 = Space parity |
| DATABITS | IN | UInt | Bits per character (Default value:1):  1 = 8 data bits, 2 = 7 data bits |
| STOPBITS | IN | UInt | Stop bits (Default value: 1):  1 = 1 stop bit, 2 = 2 stop bits |
| FLOWCTRL | IN | UInt | Flow control (Default value: 1):  1 = No flow control, 2 = XON/XOFF, 3 = Hardware RTS always ON, 4 = Hardware RTS  switched |
| XONCHAR | IN | Char | Specifies the character that is used as the XON character. This is typically a DC1 character (16#11). This parameter is only evaluated if flow control is enabled. (Default value: 16#11) |
| XOFFCHAR | IN | Char | Specifies the character that is used as the XOFF character. This is typically a DC3 character (116#3). This parameter is only evaluated if flow control is enabled. (Default value: 16#13) |
| XWAITIME | IN | UInt | Specifies how long to wait for a XON character after receiving a XOFF character, or how long to wait for the CTS signal after enabling RTS (0 to 65535 ms). This parameter is only evaluated if flow control is enabled. (Default value: 2000) |
| DONE | OUT | Bool | TRUE for one execution after the last request was completed with no error |
| ERROR | OUT | Bool | TRUE for one execution after the last request was completed with an error |
| STATUS | OUT | Word | Execution condition code (Default value: 0) |

Table 3. Condition codes

| **STATUS (W#16#....)** | **Description** |
| --- | --- |
| 80A0 | Specific protocol does not exist. |
| 80A1 | Specific baud rate does not exist. |
| 80A2 | Specific parity option does not exist. |
| 80A3 | Specific number of data bits does not exist. |
| 80A4 | Specific number of stop bits does not exist. |
| 80A5 | Specific type of flow control does not exist. |
| 80A6 | Wait time is 0 and flow control enabled |
| 80A7 | XON and XOFF are illegal values (for example, the same value) |

---

#### SEND_CFG (Configure serial transmission parameters dynamically)

Table 1. SEND\_CFG (Send Configuration) instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"SEND\_CFG\_DB"(    REQ:=\_bool\_in\_,    PORT:=\_uint\_in\_,    RTSONDLY:=\_uint\_in\_,    RTSOFFDLY:=\_uint\_in\_,    BREAK:=\_uint\_in\_,    IDLELINE:=\_uint\_in\_,    DONE=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_);** | SEND\_CFG allows the dynamic configuration of serial transmission parameters for a PtP communication port. Any queued messages within a CM or CB are discarded when SEND\_CFG is executed. |

1 STEP 7 automatically creates the DB when you insert the instruction.

You can set up the initial static configuration of the port in the device configuration properties, or just use the default values. You can execute the SEND\_CFG instruction in your program to change the configuration.

The SEND\_CFG configuration changes are not permanently stored in the CPU. The parameters configured in the device configuration are restored when the CPU transitions from RUN to STOP mode and after a power cycle. See [Configuring transmit (send) parameters](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/mi0ZQs72yHnZb7VuReqWJQ?section=X358ac999dfa5ea1132da97fc314beb32).

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Activate the configuration change on the rising edge of this input.. (Default value: False) |
| PORT | IN | PORT | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. (Default value: 0) |
| RTSONDLY | IN | UInt | Number of milliseconds to wait after enabling RTS before any Tx data transmission occurs. This parameter is only valid when hardware flow control is enabled. The valid range is 0 - 65535 ms. A value of 0 disables the feature. (Default value: 0) |
| RTSOFFDLY | IN | UInt | Number of milliseconds to wait after the Tx data transmission occurs before RTS is disabled: This parameter is only valid when hardware flow control is enabled. The valid range is 0 - 65535 ms. A value of 0 disables the feature. (Default value: 0) |
| BREAK | IN | UInt | This parameter specifies that a break will be sent upon the start of each message for the specified number of bit times. The maximum is 65535 bit times up to an eight second maximum. A value of 0 disables the feature. (Default value: 12) |
| IDLELINE | IN | UInt | This parameter specifies that the line will remain idle for the specified number of bit times before the start of each message. The maximum is 65535 bit times up to an eight second maximum. A value of 0 disables the feature. (Default value: 12) |
| DONE | OUT | Bool | TRUE for one execution after the last request was completed with no error |
| ERROR | OUT | Bool | TRUE for one execution after the last request was completed with an error |
| STATUS | OUT | Word | Execution condition code (Default value: 0) |

Table 3. Condition codes

| **STATUS (W#16#....)** | **Description** |
| --- | --- |
| 80B0 | Transmit interrupt configuration is not allowed. |
| 80B1 | Break time is greater than the maximum allowed value. |
| 80B2 | Idle time is greater than the maximum allowed value. |

---

#### RCV_CFG (Configure serial receive parameters dynamically)

Table 1. RCV\_CFG (Receive Configuration) instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"RCV\_CFG\_DB"(    REQ:=\_bool\_in\_,    PORT:=\_uint\_in\_,    CONDITIONS:=\_struct\_in\_,    DONE=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_);** | RCV\_CFG performs dynamic configuration of serial receiver parameters for a PtP communication port. This instruction configures the conditions that signal the start and end of a received message. Any queued messages within a CM or CB are discarded when RCV\_CFG is executed. |

1 STEP 7 automatically creates the DB when you insert the instruction.

You can set up the initial static configuration of the communication port in the device configuration properties, or just use the default values. You can execute the RCV\_CFG instruction in your program to change the configuration.

The RCV\_CFG configuration changes are not permanently stored in the CPU. The parameters configured in the device configuration are restored when the CPU transitions from RUN to STOP mode and after a power cycle. See [Configuring receive parameters](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/nQZx5GyPj9l1lFJ~TPSwGw?section=X0dfba602007d73e8c4bd054e1e16900d) for more information.

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Activate the configuration change on the rising edge of this input. (Default value: False) |
| PORT | IN | PORT | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. (Default value: 0) |
| CONDITIONS | IN | CONDITIONS | The Conditions data structure specifies the starting and ending message conditions as described below. |
| DONE | OUT | Bool | TRUE for one scan, after the last request was completed with no error |
| ERROR | OUT | Bool | TRUE for one scan, after the last request was completed with an error |
| STATUS | OUT | Word | Execution condition code (Default value: 0) |

## Start conditions for the RCV\_PTP instruction

The RCV\_PTP instruction uses the configuration specified by the RCV\_CFG instruction to determine the beginning and ending of point-to-point communication messages. The start of a message is determined by the start conditions. The start of a message can be determined by one or a combination of start conditions. If more than one start condition is specified, all the conditions must be satisfied before the message is started.

See the topic "[Configuring receive parameters](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/nQZx5GyPj9l1lFJ~TPSwGw?section=X0dfba602007d73e8c4bd054e1e16900d)" for a description of the message start conditions.

## Parameter CONDITIONS data type structure part 1 (start conditions)

Table 3. CONDITIONS structure for START conditions

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| STARTCOND | IN | UInt | Specifies the start condition (Default value: 1)   - 01H - Start Char - 02H - Any Char - 04H - Line Break - 08H - Idle Line - 10H - Sequence 1 - 20H - Sequence 2 - 40H - Sequence 3 - 80H - Sequence 4 |
| IDLETIME | IN | UInt | The number of bit times required for idle line timeout. (Default value: 40). Only used with an idle line condition. 0 to 65535 |
| STARTCHAR | IN | Byte | The start character used with the start character condition. (Default value: B#16#2) |
| SEQ[1].CTL | IN | Byte | Sequence 1 ignore/compare control for each character: (Default value: B#16#0)  These are the enabling bits for each character in start sequence   - 01H - Character 1 - 02H - Character 2 - 04H - Character 3 - 08H - Character 4 - 10H - Character 5   Disabling the bit associated with a character means any character will match, in this sequence position. |
| SEQ[1].STR | IN | Char[5] | Sequence 1 start characters (5 characters). Default value: 0 |
| SEQ[2].CTL | IN | Byte | Sequence 2 ignore/compare control for each character. Default value: B#16#0) |
| SEQ[2].STR | IN | Char[5] | Sequence 2 start characters (5 characters). Default value: 0 |
| SEQ[3].CTL | IN | Byte | Sequence 3 ignore/compare control for each character. Default value: B#16#0 |
| SEQ[3].STR | IN | Char[5] | Sequence 3 start characters (5 characters). Default value: 0 |
| SEQ[4].CTL | IN | Byte | Sequence 4 ignore/compare control for each character. Default value: B#16#0 |
| SEQ[4].STR | IN | Char[5] | Sequence 4 start characters (5 characters), Default value: 0 |

## Example

Consider the following received hexadecimal coded message: "**68** 10 aa **68** bb 10 aa 16" and the configured start sequences shown in the table below. Start sequences begin to be evaluated when the first 68H character is successfully received. Upon successfully receiving the fourth character (the second 68H), then start condition 1 is satisfied. Once the start conditions are satisfied, the evaluation of the end conditions begins.

The start sequence processing can be terminated due to various parity, framing, or inter-character timing errors. These errors result in no received message, because the start condition was not satisfied.

Table 4. Start conditions

| **Start condition** | **First Character** | **First Character +1** | **First Character +2** | **First Character +3** | **First Character +4** |
| --- | --- | --- | --- | --- | --- |
| 1 | **68**H | xx | xx | **68**H | xx |
| 2 | 10H | aaH | xx | xx | xx |
| 3 | dcH | aaH | xx | xx | xx |
| 4 | e5H | xx | xx | xx | xx |

## End conditions for the RCV\_PTP instruction

The end of a message is determined by the specification of end conditions. The end of a message is determined by the first occurrence of one or more configured end conditions. The section "Message end conditions" in the topic "[Configuring receive parameters](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/nQZx5GyPj9l1lFJ~TPSwGw?section=X0dfba602007d73e8c4bd054e1e16900d)" describes the end conditions that you can configure in the RCV\_CFG instruction.

You can configure the end conditions in either the properties of the communication interface in the device configuration, or from the RCV\_CFG instruction. Whenever the CPU transitions from STOP to RUN, the receive parameters (both start and end conditions) return to the device configuration settings. If the STEP 7 user program executes RCV\_CFG, then the settings are changed to the RCV\_CFG conditions.

## Parameter CONDITIONS data type structure part 2 (end conditions)

Table 5. CONDITIONS structure for END conditions

| **Parameter** | **Parameter type** | **Data type** | **Description** |
| --- | --- | --- | --- |
| ENDCOND | IN | UInt  0 | This parameter specifies message end condition:   - 01H - Response time - 02H - Message time - 04H - Inter-character gap - 08H - Maximum length - 10H - N + LEN + M - 20H - Sequence |
| MAXLEN | IN | UInt  1 | Maximum message length: Only used when the maximum length end condition is selected. 1 to 1024 bytes |
| N | IN | UInt  0 | Byte position within the message of the length field. Only used with the N + LEN + M end condition. 1 to 1022 bytes |
| LENGTHSIZE | IN | UInt  0 | Size of the length field (1, 2, or 4 bytes). Only used with the N + LEN + M end condition. |
| LENGTHM | IN | UInt  0 | Specify the number of characters following the length field that are not included in the value of the length field. This is only used with the N + LEN + M end condition. 0 to 255 bytes |
| RCVTIME | IN | UInt  200 | Specify how long to wait for the first character to be received. The receive operation will be terminated with an error if a character is not successfully received within the specified time. This is only used with the response time condition. (0 to 65535 bit times with an 8 second maximum)  This parameter is not a message end condition since evaluation terminates when the first character of a response is received. It is an end condition only in the sense that it terminates a receiver operation because no response is received when a response is expected. You must select a separate end condition. |
| MSGTIME | IN | UInt  200 | Specify how long to wait for the entire message to be completely received once the first character has been received. This parameter is only used when the message timeout condition is selected. (0 to 65535 milliseconds) |
| CHARGAP | IN | UInt  12 | Specify the number of bit times between characters. If the number of bit times between characters exceeds the specified value, then the end condition will be satisfied. This is only used with the inter-character gap condition. (0 to 65535 bit times up to 8 second maximum) |
| SEQ.CTL | IN | Byte  B#16#0 | Sequence 1 ignore/compare control for each character:  These are the enabling bits for each character for the end sequence. Character 1 is bit 0, character 2 is bit 1, …, character 5 is bit 4. Disabling the bit associated with a character means any character will match, in this sequence position. |
| SEQ.STR | IN | Char[5]  0 | Sequence 1 start characters (5 characters) |

Table 6. Condition codes

| **STATUS (W#16#....)** | **Description** |
| --- | --- |
| 80C0 | Illegal start condition selected |
| 80C1 | Illegal end condition selected, no end condition selected |
| 80C2 | Receive interrupt enabled and this is not possible. |
| 80C3 | Maximum length end condition is enabled and max length is 0 or > 1024. |
| 80C4 | Calculated length is enabled and N is >= 1023. |
| 80C5 | Calculated length is enabled and length is not 1, 2 or 4. |
| 80C6 | Calculated length is enabled and M value is > 255. |
| 80C7 | Calculated length is enabled and calculated length is > 1024. |
| 80C8 | Response timeout is enabled and response timeout is zero. |
| 80C9 | Inter-character gap timeout is enabled and it is zero. |
| 80CA | Idle line timeout is enabled and it is zero. |
| 80CB | End sequence is enabled but all chars are "don't care". |
| 80CC | Start sequence (any one of 4) is enabled but all characters are "don't care". |

---

#### SEND_PTP (Transmit send buffer data)

Table 1. SEND\_PTP (Send Point-to-Point data) instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"SEND\_PTP\_DB"(    REQ:=\_bool\_in\_,    PORT:=\_uint\_in\_,    BUFFER:=\_variant\_in\_,    LENGTH:=\_uint\_in\_,    PTRCL:=\_bool\_in\_,    DONE=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_);** | SEND\_PTP initiates the transmission of the data and transfers the assigned buffer to the communication interface. The CPU program continues while the CM or CB sends the data at the assigned baud rate. Only one send operation can be pending at a given time. The CM or CB returns an error if a second SEND\_PTP is executed while the CM or CB is already transmitting a message. |

1 STEP 7 automatically creates the DB when you insert the instruction.

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Activates the requested transmission on the rising edge of this transmission enable input. This initiates transfer of the contents of the buffer to the Point-to-Point communication interface. (Default value: False) |
| PORT | IN | PORT | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. (Default value: 0) |
| BUFFER | IN | Variant | This parameter points to the starting location of the transmit buffer. (Default value: 0)  **Note:** Boolean data or Boolean arrays are not supported. |
| LENGTH 1 | IN | UInt | Transmitted frame length in bytes (Default value: 0)  When transmitting a complex structure, always use a length of 0. |
| PTRCL | IN | Bool | Reserved for future use |
| DONE | OUT | Bool | TRUE for one scan, after the last request was completed with no error |
| ERROR | OUT | Bool | TRUE for one scan, after the last request was completed with an error |
| STATUS | OUT | Word | Execution condition code (Default value: 0) |

1 Optional parameter: Click the arrow at the bottom of a LAD/FBD box to expand the box and include this parameter.

While a transmit operation is in progress, the DONE and ERROR outputs are FALSE. When a transmit operation is complete, either the DONE or the ERROR output will be set TRUE to show the status of the transmit operation. While DONE or ERROR is TRUE, the STATUS output is valid.

The instruction returns a status of 16#7001 if the communication interface accepts the transmit data. Subsequent SEND\_PTP executions return 16#7002, if the CM or CB is still busy transmitting. When the transmit operation is complete, the CM or CB returns the status of the transmit operation as 16#0000 (if no errors occurred). Subsequent executions of SEND\_PTP with REQ low return a status of 16#7000 (not busy).

The following diagrams show the relationship of the output values to REQ. This assumes that the instruction is called periodically to check for the status of the transmission process. In the diagram below, it is assumed that the instruction is called every scan (represented by the STATUS values).

Figure 1. [![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/sCBcV0R5KXVbAyqsAKN6iA-VBkTPlmjVZAl17lebjV9hA)

The following diagram shows how the DONE and STATUS parameters are valid for only one scan if the REQ line is pulsed (for one scan) to initiate the transmit operation.

Figure 2. [![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/fGGQUUteV_qO6uPBNvTQlg-VBkTPlmjVZAl17lebjV9hA)

The following diagram shows the relationship of DONE, ERROR and STATUS parameters when there is an error.

Figure 3. [![](data:image/png;base64,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)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/NU6ddTPkTmsC4d~boaIfQA-VBkTPlmjVZAl17lebjV9hA)

The DONE, ERROR and STATUS values are only valid until SEND\_PTP executes again with the same instance DB.

Table 3. Condition codes

| **STATUS (W#16#....)** | **Description** |
| --- | --- |
| 80D0 | New request while transmitter active |
| 80D1 | Transmit aborted because of no CTS within wait time |
| 80D2 | Transmit aborted because of no DSR from the DCE device |
| 80D3 | Transmit aborted because of queue overflow (transmit more than 1024 bytes) |
| 80D5 | Reverse bias signal (wire break condition) |
| 833A | The DB for the BUFFER parameter does not exist. |

---

#### RCV_PTP (Enable receive messages)

Table 1. RCV\_PTP (Receive Point-to-Point) instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"RCV\_PTP\_DB"(    EN\_R:=\_bool\_in\_,    PORT:=\_uint\_in\_,    BUFFER:=\_variant\_in\_,    NDR=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    LENGTH=>\_uint\_out\_);** | RCV\_PTP checks for messages that have been received in the CM or CB. If a message is available, it will be transferred from the CM or CB to the CPU. An error returns the appropriate STATUS value. |

1 STEP 7 automatically creates the DB when you insert the instruction.

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| EN\_R | IN | Bool | When this input is TRUE and a message is available, the message is transferred from the CM or CB to the BUFFER. When EN\_R is FALSE, the CM or CB is checked for messages and NDR, ERROR and STATUS output are updated, but the message is not transferred to the BUFFER. (Default value: 0) |
| PORT | IN | PORT | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. (Default value: 0) |
| BUFFER | IN | Variant | This parameter points to the starting location of the receive buffer. This buffer should be large enough to receive the maximum length message.  Boolean data or Boolean arrays are not supported. (Default value: 0) |
| NDR | OUT | Bool | TRUE for one execution when new data is ready and operation is complete with no errors. |
| ERROR | OUT | Bool | TRUE for one execution after the operation was completed with an error. |
| STATUS | OUT | Word | Execution condition code (Default value: 0) |
| LENGTH | OUT | UInt | Length of the returned message in bytes (Default value: 0) |

Note the following correlation between the EN\_R input and the message buffer of the RCV\_PTP instruction:

Input EN\_R controls the copy of a received message to the BUFFER.

When the EN\_R input is TRUE and a message is available, the CPU transfers the message from the CM or CB to the BUFFER and updates the NDR, ERROR, STATUS, and LENGTH outputs.

When EN\_R is FALSE, the CPU checks the CM or CB for messages and updates the NDR, ERROR, and STATUS outputs, but does not transfer the message to the BUFFER. (Note that the default value of EN\_R is FALSE.)

The recommended practice is to set EN\_R to TRUE and control execution of the RCV\_PTP instruction with the EN input.

The STATUS value is valid when either NDR or ERROR is TRUE. The STATUS value provides the reason for termination of the receive operation in the CM or CB. This is typically a positive value, indicating that the receive operation was successful and that the receive process terminated normally. If the STATUS value is negative (the Most Significant Bit of the hexadecimal value is set), the receive operation was terminated for an error condition such as parity, framing, or overrun errors.

Each PtP communication interface can buffer up to a maximum of 1024 bytes. This could be one large message or several smaller messages. If more than one message is available in the CM or CB, the RCV\_PTP instruction returns the oldest message available. A subsequent RCV\_PTP instruction execution returns the next oldest message available.

Table 3. Condition codes

| **STATUS (W#16#...)** | **Description** |
| --- | --- |
| 0000 | No buffer present |
| 0094 | Message terminated due to received maximum character length |
| 0095 | Message terminated because of message timeout |
| 0096 | Message terminated because of inter-character timeout |
| 0097 | Message terminated because of response timeout |
| 0098 | Message terminated because the "N+LEN+M" length condition was satisfied |
| 0099 | Message terminated because of end sequence was satisfied |
| 80E0 | Message terminated because the receive buffer is full |
| 80E1 | Message terminated due to parity error |
| 80E2 | Message terminated due to framing error |
| 80E3 | Message terminated due to overrun error |
| 80E4 | Message terminated because calculated length exceeds buffer size |
| 80E5 | Reverse bias signal (wire break condition) |
| 833A | The DB for the BUFFER parameter does not exist. |

---

#### RCV_RST (Delete receive buffer)

Table 1. RCV\_RST (Receiver Reset) instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"RCV\_RST\_DB"(    REQ:=\_bool\_in\_,    PORT:=\_uint\_in\_,    DONE=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_);** | RCV\_RST clears the receive buffers in the CM or CB. |

1 STEP 7 automatically creates the DB when you insert the instruction.

Table 2. Data types for parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Activates the receiver reset on the rising edge of this enable input (Default value: False) |
| PORT | IN | PORT | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. (Default value: 0) |
| DONE | OUT | Bool | When TRUE for one scan, indicates that the last request was completed without errors. |
| ERROR | OUT | Bool | When TRUE, shows that the last request was completed with errors. Also, when this output is TRUE, the STATUS output will contain related error codes. |
| STATUS | OUT | Word | Error code (Default value: 0)  See [Common parameters for Point-to-Point instructions](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/stMdI~i5k1wrAf398GR3AA?section=X03af0d734df93e2cc6a84931ce873f8e) for communication status codes. |

Note:

You might want to use the RCV\_RST instruction to be sure the message buffers are clear following a communications error, or after changing a communication parameter such as the baud rate. Executing RCV\_RST causes the module to clear all of the internal message buffers. After clearing the message buffers, you can be assured that when your program executes a subsequent receive instruction, the messages it returns are new messages and not old messages from some time prior to the RCV\_RST call.

---

#### SGN_GET (Query RS-232 signals)

Table 1. SGN\_GET (Get RS232 signals) instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"SGN\_GET\_DB"(    REQ:=\_bool\_in\_,    PORT:=\_uint\_in\_,    NDR=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    DTR=>\_bool\_out\_,    DSR=>\_bool\_out\_,    RTS=>\_bool\_out\_,    CTS=>\_bool\_out\_,    DCD=>\_bool\_out\_,    RING=>\_bool\_out\_);** | SGN\_GET reads the current states of RS232 communication signals.  This function is valid only for the RS232 CM. |

1 STEP 7 automatically creates the DB when you insert the instruction.

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Get RS232 signal state values on the rising edge of this input (Default value: False) |
| PORT | IN | PORT | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. |
| NDR | OUT | Bool | TRUE for one scan, when new data is ready and the operation is complete with no errors |
| ERROR | OUT | Bool | TRUE for one scan, after the operation was completed with an error |
| STATUS | OUT | Word | Execution condition code (Default value: 0) |
| DTR | OUT | Bool | Data terminal ready, module ready (output). Default value: False |
| DSR | OUT | Bool | Data set ready, communication partner ready (input). Default value: False |
| RTS | OUT | Bool | Request to send, module ready to send (output). Default value: False |
| CTS | OUT | Bool | Clear to send, communication partner can receive data (input). Default value: False |
| DCD | OUT | Bool | Data carrier detect, receive signal level (always False, not supported) |
| RING | OUT | Bool | Ring indicator, indication of incoming call (always False, not supported) |

Table 3. Condition codes

| **STATUS (W#16#....)** | **Description** |
| --- | --- |
| 80F0 | CM or CB is RS485 and no signals are available |

---

#### SGN_SET (Set RS-232 signals)

Table 1. SGN\_SET (Set RS232 signals) instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"SGN\_SET\_DB"(    REQ:=\_bool\_in\_,    PORT:=\_uint\_in\_,    SIGNAL:=\_byte\_in\_,    RTS:=\_bool\_in\_,    DTR:=\_bool\_in\_,    DSR:=\_bool\_in\_,    DONE=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_);** | SGN\_SET sets the states of RS232 communication signals.  This function is valid only for the RS232 CM. |

1 STEP 7 automatically creates the DB when you insert the instruction.

Table 2. Data types for parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Start the set RS232 signals operation, on the rising edge of this input (Default value: False) |
| PORT | IN | PORT | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. (Default value: 0) |
| SIGNAL | IN | Byte | Selects which signal to set: (multiple allowed). Default value: 0   - 01H = Set RTS - 02H = Set DTR - 04H = Set DSR |
| RTS | IN | Bool | Request to send, module ready to send value to set (true or false), Default value: False |
| DTR | IN | Bool | Data terminal ready, module ready to send value to set (true or false). Default value: False |
| DSR | IN | Bool | Data set ready (only applies to DCE type interfaces), not used. |
| DONE | OUT | Bool | TRUE for one execution after the last request was completed with no error |
| ERROR | OUT | Bool | TRUE for one execution after the last request was completed with an error |
| STATUS | OUT | Word | Execution condition code (Default value: 0) |

Table 3. Condition codes

| **STATUS (W#16#....)** | **Description** |
| --- | --- |
| 80F0 | CM or CB is RS485 and no signals can be set |
| 80F1 | Signals cannot be set because of Hardware flow control |
| 80F2 | Cannot set DSR because module is DTE |
| 80F3 | Cannot set DTR because module is DCE |

---

## Legacy USS communication (CM/CB 1241 only)


---

### Overview

The USS instructions control the operation of motor drives which support the universal serial interface (USS) protocol. You can use the USS instructions to communicate with multiple drives through RS485 connections to CM 1241 RS485 communication modules or a CB 1241 RS485 communication board. Up to three CM 1241 RS422/RS485 modules and one CB 1241 RS485 board can be installed in a S7-1200 CPU. Each RS485 port can operate up to sixteen drives.

The USS protocol uses a master-slave network for communications over a serial bus. The master uses an address parameter to send a message to a selected slave. A slave itself can never transmit without first receiving a request to do so. Direct message transfer between the individual slaves is not possible. USS communication operates in half-duplex mode. The following USS illustration shows a network diagram for an example drive application.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/JSqJjUH_o6eZyVKmumZ~Fg-VBkTPlmjVZAl17lebjV9hA/content?v=eaf8b4a12f5f771e)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/JSqJjUH_o6eZyVKmumZ~Fg-VBkTPlmjVZAl17lebjV9hA)

Note that STEP 7 provides different versions of the USS instructions. For information on instruction versions, refer to [Use Instruction versions](https://support.industry.siemens.com/cs/ww/en/view/109798671/113722878475) in the STEP 7 Information System.

## Requirements for using the USS protocol

The four USS instructions use 2 FBs and 2 FCs to support the USS protocol. For each USS network, one instance data block (DB) is used for USS\_Port\_Scan and one instance data block for all calls of USS\_Drive\_Conrol. For further requirements, refer to the topic "[Requirements for using the USS protocol](https://support.industry.siemens.com/cs/ww/en/view/109798671/140076559243)" in the STEP 7 Information System or on Siemens Industry Online Support.

---

### Legacy USS instructions


---

#### USS_PORT (Edit communication using USS network) instruction

Table 1. USS\_PORT instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **USS\_PORT(    PORT:=\_uint\_in\_,    BAUD:=\_dint\_in\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    USS\_DB:=\_fbtref\_inout\_);** | The USS\_PORT instruction handles communication over a USS network. |

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| PORT | IN | Port | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. |
| BAUD | IN | DInt | The baud rate used for USS communication. |
| USS\_DB | INOUT | USS\_BASE | The name of the instance DB that is created and initialized when a USS\_DRV instruction is placed in your program. |
| ERROR | OUT | Bool | When true, this output indicates that an error has occurred and the STATUS output is valid. |
| STATUS | OUT | Word | The status value of the request indicates the result of the scan or initialization. Additional information is available in the "USS\_Extended\_Error" variable for some status codes. |

Typically, there is only one USS\_PORT instruction per PtP communication port in the program, and each call of this function handles a transmission to or from a single drive. All USS functions associated with one USS network and PtP communication port must use the same instance DB.

Your program must execute the USS\_PORT instruction often enough to prevent drive timeouts. USS\_PORT is usually called from a cyclic interrupt OB to prevent drive timeouts and keep the most recent USS data updates available for USS\_DRV calls.

---

#### USS_DRV (Swap data with drive) instruction

Table 1. USS\_DRV instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
| Default view | **"USS\_DRV\_DB"(    RUN:=\_bool\_in\_,    OFF2:=\_bool\_in\_,    OFF3:=\_bool\_in\_,    F\_ACK:=\_bool\_in\_,    DIR:=\_bool\_in\_,    DRIVE:=\_usint\_in\_,    PZD\_LEN:=\_usint\_in\_,    SPEED\_SP:=\_real\_in\_,    CTRL3:=\_word\_in\_,    CTRL4:=\_word\_in\_,    CTRL5:=\_word\_in\_,    CTRL6:=\_word\_in\_,    CTRL7:=\_word\_in\_,    CTRL8:=\_word\_in\_,    NDR=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    RUN\_EN=>\_bool\_out\_,    D\_DIR=>\_bool\_out\_,    INHIBIT=>\_bool\_out\_,    FAULT=>\_bool\_out\_,    SPEED=>\_real\_out\_,    STATUS1=>\_word\_out\_,    STATUS3=>\_word\_out\_,    STATUS4=>\_word\_out\_,    STATUS5=>\_word\_out\_,    STATUS6=>\_word\_out\_,    STATUS7=>\_word\_out\_,    STATUS8=>\_word\_out\_);** | The USS\_DRV instruction exchanges data with a drive by creating request messages and interpreting the drive response messages. A separate function block should be used for each drive, but all USS functions associated with one USS network and PtP communication port must use the same instance data block. You must create the DB name when you place the first USS\_DRV instruction and then reference the DB that was created by the initial instruction usage.  STEP 7 automatically creates the DB when you insert the instruction. |
| Expanded view |

1 LAD and FBD: Expand the box to reveal all the parameters by clicking the bottom of the box. The parameter pins that are grayed are optional and parameter assignment is not required.

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| RUN | IN | Bool | Drive start bit: When true, this input enables the drive to run at the preset speed. When RUN goes to false while a drive is running, the motor will be ramped down to a stop. This behavior differs from the dropping power (OFF2) or braking the motor (OFF3). |
| OFF2 | IN | Bool | Electrical stop bit: When false, this bit causes the drive to coast to a stop with no braking. |
| OFF3 | IN | Bool | Fast stop bit: When false, this bit causes a fast stop by braking the drive rather than just allowing the drive to coast to a stop. |
| F\_ACK | IN | Bool | Fault acknowledge bit: This bit is set to reset the fault bit on a drive. The bit is set after the fault is cleared to indicate to the drive it no longer needs to indicate the previous fault. |
| DIR | IN | Bool | Drive direction control: This bit is set to indicate that the direction is forward (for positive SPEED\_SP). |
| DRIVE | IN | USInt | Drive address: This input is the address of the USS drive. The valid range is drive 1 to drive 16. |
| PZD\_LEN | IN | USInt | Word length: This is the number of words of PZD data. The valid values are 2, 4, 6, or 8 words. The default value is 2. |
| SPEED\_SP | IN | Real | Speed set point: This is the speed of the drive as a percentage of configured frequency. A positive value specifies forward direction (when DIR is true). Valid range is 200.00 to -200.00. |
| CTRL3 | IN | Word | Control word 3: A value written to a user-configurable parameter on the drive. You must configure this on the drive. (optional parameter) |
| CTRL4 | IN | Word | Control word 4: A value written to a user-configurable parameter on the drive. You must configure this on the drive. (optional parameter) |
| CTRL5 | IN | Word | Control word 5: A value written to a user-configurable parameter on the drive. You must configure this on the drive. (optional parameter) |
| CTRL6 | IN | Word | Control word 6: A value written to a user-configurable parameter on the drive. You must configure this on the drive. (optional parameter) |
| CTRL7 | IN | Word | Control word 7: A value written to a user-configurable parameter on the drive. You must configure this on the drive. (optional parameter) |
| CTRL8 | IN | Word | Control word 8: A value written to a user-configurable parameter on the drive. You must configure this on the drive. (optional parameter) |
| NDR | OUT | Bool | New data ready: When true, the bit indicates that the outputs contain data from a new communication request. |
| ERROR | OUT | Bool | Error occurred: When true, this indicates that an error has occurred and the STATUS output is valid. All other outputs are set to zero on an error. Communication errors are only reported on the USS\_PORT instruction ERROR and STATUS outputs. |
| STATUS | OUT | Word | The status value of the request indicates the result of the scan. This is not a status word returned from the drive. |
| RUN\_EN | OUT | Bool | Run enabled: This bit indicates whether the drive is running. |
| D\_DIR | OUT | Bool | Drive direction: This bit indicates whether the drive is running forward. |
| INHIBIT | OUT | Bool | Drive inhibited: This bit indicates the state of the inhibit bit on the drive. |
| FAULT | OUT | Bool | Drive fault: This bit indicates that the drive has registered a fault. You must fix the problem and then set the F\_ACK bit to clear this bit when set. |
| SPEED | OUT | Real | Drive Current Speed (scaled value of drive status word 2): The value of the speed of the drive as a percentage of configured speed. |
| STATUS1 | OUT | Word | Drive Status Word 1: This value contains fixed status bits of a drive. |
| STATUS3 | OUT | Word | Drive Status Word 3: This value contains a user-configurable status word on the drive. |
| STATUS4 | OUT | Word | Drive Status Word 4: This value contains a user-configurable status word on the drive. |
| STATUS5 | OUT | Word | Drive Status Word 5: This value contains a user-configurable status word on the drive. |
| STATUS6 | OUT | Word | Drive Status Word 6: This value contains a user-configurable status word on the drive. |
| STATUS7 | OUT | Word | Drive Status Word 7: This value contains a user-configurable status word on the drive. |
| STATUS8 | OUT | Word | Drive Status Word 8: This value contains a user-configurable status word on the drive. |

When the initial USS\_DRV execution occurs, the drive indicated by the USS address (parameter DRIVE) is initialized in the Instance DB. After this initialization, subsequent executions of USS\_PORT can begin communication to the drive at this drive number.

Changing the drive number requires a CPU STOP-to-RUN mode transition that initializes the instance DB. Input parameters are configured into the USS TX message buffer and outputs are read from a "previous" valid response buffer if any exists. There is no data transmission during USS\_DRV execution. Drives communicate when USS\_PORT is executed. USS\_DRV only configures the messages to be sent and interprets data that might have been received from a previous request.

You can control the drive direction of rotation using either the DIR input (Bool) or using the sign (positive or negative) with the SPEED\_SP input (Real). The following table indicates how these inputs work together to determine the drive direction, assuming the motor is wired for forward rotation.

Table 3. Interaction of the SPEED\_SP and DIR parameters

| **SPEED\_SP** | **DIR** | **Drive rotation direction** |
| --- | --- | --- |
| Value > 0 | 0 | Reverse |
| Value > 0 | 1 | Forward |
| Value < 0 | 0 | Forward |
| Value < 0 | 1 | Reverse |

---

#### USS_RPM (Readout parameters from the drive) instruction

Table 1. USS\_RPM instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **USS\_RPM(REQ:=\_bool\_in\_,    DRIVE:=\_usint\_in\_,    PARAM:=\_uint\_in\_,    INDEX:=\_uint\_in\_,    DONE=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    VALUE=>\_variant\_out\_,    USS\_DB:=\_fbtref\_inout\_);** | The USS\_RPM instruction reads a parameter from a drive. All USS functions associated with one USS network and PtP communication port must use the same data block. USS\_RPM must be called from a main program cycle OB. |

Table 2. Data types for the parameters

| **Parameter type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Send request: When true, REQ indicates that a new read request is desired. This is ignored if the request for this parameter is already pending. |
| DRIVE | IN | USInt | Drive address: DRIVE is the address of the USS drive. The valid range is drive 1 to drive 16. |
| PARAM | IN | UInt | Parameter number: PARAM designates which drive parameter is written. The range of this parameter is 0 to 2047. On some drives, the most significant byte can access PARAM values greater than 2047. See your drive manual for details on how to access an extended range. |
| INDEX | IN | UInt | Parameter index: INDEX designates which Drive Parameter index is to be written. A 16-bit value where the Least Significant Byte is the actual index value with a range of (0 to 255). The Most Significant Byte may also be used by the drive and is drive-specific. See your drive manual for details. |
| USS\_DB | INOUT | USS\_BASE | The name of the instance DB that is created and initialized when a USS\_DRV instruction is placed in your program. |
| VALUE | IN | Word, Int, UInt, DWord, DInt, UDInt, Real | This is the value of the parameter that was read and is valid only when the DONE bit is true. |
| DONE1 | OUT | Bool | When true, indicates that the VALUE output holds the previously requested read parameter value. This bit is set when USS\_DRV sees the read response data from the drive. This bit is reset when either: you request the response data via another USS\_RPM poll, or on the second of the next two calls to USS\_DRV |
| ERROR | OUT | Bool | Error occurred: When true, ERROR indicates that an error has occurred and the STATUS output is valid. All other outputs are set to zero on an error. Communication errors are only reported on the USS\_PORT instruction ERROR and STATUS outputs. |
| STATUS | OUT | Word | STATUS indicates the result of the read request. Additional information is available in the "USS\_Extended\_Error" variable for some status codes. |

1 The DONE bit indicates that valid data has been read from the referenced motor drive and delivered to the CPU. It does not indicate that the USS library is capable of immediately reading another parameter. A blank PKW request must be sent to the motor drive and must also be acknowledged by the instruction before the parameter channel for the specific drive becomes available for use. Immediately calling a USS\_RPM or USS\_WPM FC for the specified motor drive will result in a 0x818A error.

---

#### USS_WPM (Change parameters in the drive) instruction

Note:

**EEPROM write operations (for the EEPROM inside a USS drive)**

Do not overuse the EEPROM permanent write operation. Minimize the number of EEPROM write operations to extend the EEPROM life.

Table 1. USS\_WPM instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **USS\_WPM(REQ:=\_bool\_in\_,    DRIVE:=\_usint\_in\_,    PARAM:=\_uint\_in\_,    INDEX:=\_uint\_in\_,    EEPROM:=\_bool\_in\_,    VALUE:=\_variant\_in\_,    DONE=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    USS\_DB:=\_fbtref\_inout\_);** | The USS\_WPM instruction modifies a parameter in the drive. All USS functions associated with one USS network and PtP communication port must use the same data block.  USS\_WPM must be called from a main program cycle OB. |

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | Send request: When true, REQ indicates that a new write request is desired. This is ignored if the request for this parameter is already pending. |
| DRIVE | IN | USInt | Drive address: DRIVE is the address of the USS drive. The valid range is drive 1 to drive 16. |
| PARAM | IN | UInt | Parameter number: PARAM designates which drive parameter is written. The range of this parameter is 0 to 2047. On some drives, the most significant byte can access PARAM values greater than 2047. See your drive manual for details on how to access an extended range. |
| INDEX | IN | UInt | Parameter index: INDEX designates which Drive Parameter index is to be written. A 16-bit value where the least significant byte is the actual index value with a range of (0 to 255). The most significant byte may also be used by the drive and is drive-specific. See your drive manual for details. |
| EEPROM | IN | Bool | Store To Drive EEPROM: When true, a write drive parameter transaction will be stored in the drive EEPROM. If false, the write is temporary and will not be retained if the drive is power cycled. |
| VALUE | IN | Word, Int, UInt, DWord, DInt, UDInt, Real | The value of the parameter that is to be written. It must be valid on the transition of REQ. |
| USS\_DB | INOUT | USS\_BASE | The name of the instance DB that is created and initialized when a USS\_DRV instruction is placed in your program. |
| DONE1 | OUT | Bool | When true, DONE indicates that the input VALUE has been written to the drive. This bit is set when USS\_DRV sees the write response data from the drive. This bit is reset when either you request the response data via another USS\_WPM poll, or on the second of the next two calls to USS\_DRV |
| ERROR | OUT | Bool | When true, ERROR indicates that an error has occurred and the STATUS output is valid. All other outputs are set to zero on an error. Communication errors are only reported on the USS\_PORT instruction ERROR and STATUS outputs. |
| STATUS | OUT | Word | STATUS indicates the result of the write request. Additional information is available in the "USS\_Extended\_Error" variable for some status codes. |

1 The DONE bit indicates that valid data has been read from the referenced motor drive and delivered to the CPU. It does not indicate that the USS library is capable of immediately reading another parameter. A blank PKW request must be sent to the motor drive and must also be acknowledged by the instruction before the parameter channel for the specific drive becomes available for use. Immediately calling a USS\_RPM or USS\_WPM FC for the specified motor drive will result in a 0x818A error.

---

### Legacy USS status codes

USS instruction status codes are returned at the STATUS output of the USS functions.

Table 1. STATUS codes 1

| **STATUS (W#16#....)** | **Description** |
| --- | --- |
| 0000 | No error |
| 8180 | The length of the drive response did not match the characters received from the drive. The drive number where the error occurred is returned in the "USS\_Extended\_Error" variable. See the extended error description below this table. |
| 8181 | VALUE parameter was not a Word, Real or DWord data type. |
| 8182 | The user supplied a Word for a parameter value and received a DWord or Real from the drive in the response. |
| 8183 | The user supplied a DWord or Real for a parameter value and received a Word from the drive in the response. |
| 8184 | The response telegram from drive had a bad checksum. The drive number where the error occurred is returned in the "USS\_Extended\_Error" variable. See the extended error description below this table. |
| 8185 | Illegal drive address (valid drive address range: 1 to16) |
| 8186 | The speed set point is out of the valid range (valid speed SP range: -200% to 200%). |
| 8187 | The wrong drive number responded to the request sent. The drive number where the error occurred is returned in the "USS\_Extended\_Error" variable. See the extended error description below this table. |
| 8188 | Illegal PZD word length specified (valid range = 2, 4, 6 or 8 words) |
| 8189 | Illegal Baud Rate was specified. |
| 818A | The parameter request channel is in use by another request for this drive. |
| 818B | The drive has not responded to requests and retries. The drive number where the error occurred is returned in the "USS\_Extended\_Error" variable. See the extended error description below this table. |
| 818C | The drive returned an extended error on a parameter request operation. See the extended error description below this table. |
| 818D | The drive returned an illegal access error on a parameter request operation. See your drive manual for information of why parameter access may be limited. |
| 818E | The drive has not been initialized. This error code is returned to USS\_RPM or USS\_WPM when USS\_DRV, for that drive, has not been called at least once. This keeps the initialization on first scan of USS\_DRV from overwriting a pending parameter read or write request, since it initializes the drive as a new entry. To fix this error, call USS\_DRV for this drive number. |
| 80Ax-80Fx | Specific errors returned from PtP communication FBs called by the USS Library - These error code values are not modified by the USS library and are defined in the PtP instruction descriptions. |

1 In addition to the USS instruction errors listed above, errors can be returned from the underlying [PtP communication instructions](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/tMBOQ5UbtH6rUNYMM7aiQw?section=Xf34db9eac4f5a69d8d7356c2f37c6b0d).

For several STATUS codes, additional information is provided in the "USS\_Extended\_Error" variable of the USS\_DRV Instance DB. For STATUS codes hexadecimal 8180, 8184, 8187, and 818B, USS\_Extended\_Error contains the drive number where the communication error occurred. For STATUS code hexadecimal 818C, USS\_Extended\_Error contains a drive error code returned from the drive when using a USS\_RPM or USS\_WPM instruction.

## Example: communication errors reporting

Communication errors (STATUS = 16#818B) are only reported on the USS\_PORT instruction and not on the USS\_DRV instruction. For example, if the network is not properly terminated then it is possible for a drive to go to RUN but the USS\_DRV instruction will show all 0's for the output parameters. In this case, you can only detect the communication error on the USS\_PORT instruction. Since this error is only visible for one scan, you will need to add some capture logic as illustrated in the following example. In this example, when the error bit of the USS\_PORT instruction is TRUE, then the STATUS and the USS\_Extended\_Error values are saved into M memory. The drive number is placed in USS\_Extended\_Error variable when the STATUS code value is hexadecimal 8180, 8184, 8187, or 818B.

|  |  |
| --- | --- |
|  | **Network 1**"PortStatus"port status and"USS\_DRV\_DB".USS\_Extended\_Errorextended error code values are only valid for one program scan. The values must be captured for later processing. |
|  | **Network 2**The "PortError" contact triggers the storage of the "PortStatus" value in "LastPortStatus" and the"USS\_DRV\_DB".USS\_Extended\_Errorvalue in "LastExtError". |

## Read and write access to drive internal parameters

USS drives support read and write access to a drive's internal parameters. This feature allows remote control and configuration of the drive. Drive parameter access operations can fail due to errors such as values out of range or illegal requests for a drive's current mode. The drive generates an error code value that is returned in the "USS\_Extended\_Error" variable. This error code value is only valid for the last execution of a USS\_RPM or USS\_WPM instruction. The drive error code is put into USS\_Extended\_Error variable when the STATUS code value is hexadecimal 818C. The error code value of "USS\_Extended\_Error" depends on the drive model. See the drive's manual for a description of the extended error codes for read and write parameter operations.

---

### Legacy USS general drive setup requirements

Legacy USS general drive setup requirements consist of the following points:

- The drives must be set to use 4 PKW words.
- The drives can be configured for 2, 4, 6, or 8 PZD words.
- The number of PZD word's in the drive must match PZD\_LEN input on the USS\_DRV instruction for that drive.
- The baud rate in all the drives must match the BAUD input on the USS\_PORT instruction.
- The drive must be set for remote control.
- The drive must be set for frequency set-point to USS on COM Link.
- The drive address must be set to 1 to 16 and match the DRIVE input on the USS\_DRV block for that drive.
- The drive direction control must be set to use the polarity of the drive set-point.
- The RS485 network must be terminated properly.

USS general drive connection and setup is the same for USS instructions (V4.1) and legacy USS instructions (V4.0 and earlier). Refer to the [Example: USS general drive connection and setup](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/WrgHr5GjNGRPXT7YRjZkOg?section=X99b7495eb49d549309c93cb0e824b51e) for further information.

---

## Legacy Modbus TCP communication


---

### Overview

Prior to the release of STEP 7 V13 SP1 and the S7-1200 V4.1 CPUs, the Modbus TCP communication instructions existed with different names, and in some cases, slightly different interfaces. The general concepts apply to both sets of instructions. Refer to the individual legacy Modbus TCP instructions for programming information.

STEP 7 provides different versions of the Modbus TCP instructions. For information on instruction versions, refer to [Use Instruction versions](https://support.industry.siemens.com/cs/ww/en/view/109798671/113722878475) in the STEP 7 Information System.

---

### Legacy Modbus TCP instructions


---

#### MB_CLIENT (Communicate using PROFINET as Modbus TCP client)

Table 1. MB\_CLIENT instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"MB\_CLIENT\_DB"(    REQ:=\_bool\_in\_,    DISCONNECT:=\_bool\_in\_,    CONNECT\_ID=\_uint\_in\_,    IP\_OCTET\_1:=\_byte\_in\_,    IP\_OCTET\_2:=\_byte\_in\_,    IP\_OCTET\_3:=\_byte\_in\_,    IP\_OCTET\_4:=\_byte\_in\_,    IP\_PORT:=\_uint\_in\_,    MB\_MODE:=\_usint\_in\_,    MB\_DATA\_ADDR:=\_udint\_in\_,    MB\_DATA\_LEN:=\_uint\_in\_,    DONE=>\_bool\_out\_,    BUSY=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    MB\_DATA\_PTR:=\_variant\_inout\_);** | MB\_CLIENT communicates as a Modbus TCP client through the PROFINET connector on the S7-1200 CPU. No additional communication hardware module is required.  MB\_CLIENT can make a client-server connection, send a Modbus function request, receive a response, and control the disconnection from a Modbus TCP server. |

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | In | Bool | FALSE = No Modbus communication request  TRUE = Request to communicate with a Modbus TCP server |
| DISCONNECT | IN | Bool | The DISCONNECT parameter allows your program to control connection and disconnection with a Modbus server device.  If DISCONNECT = 0 and a connection does not exist, then MB\_CLIENT attempts to make a connection to the assigned IP address and port number.  If DISCONNECT = 1 and a connection exists, then a disconnect operation is attempted. Whenever this input is enabled, no other operation will be attempted. |
| CONNECT\_ID | IN | UInt | The CONNECT\_ID parameter must uniquely identify each connection within the PLC. Each unique instance of the MB\_CLIENT or MB\_SERVER instruction must contain a unique CONNECT\_ID parameter. |
| IP\_OCTET\_1 | IN | USInt | Modbus TCP server IP address: Octet 1  8-bit part of the 32-bit IPv4 IP address of the Modbus TCP server to which the client will connect and communicate using the Modbus TCP protocol. |
| IP\_OCTET\_2 | IN | USInt | Modbus TCP server IP address: Octet 2 |
| IP\_OCTET\_3 | IN | USInt | Modbus TCP server IP address: Octet 3 |
| IP\_OCTET\_4 | IN | USInt | Modbus TCP server IP address: Octet 4 |
| IP\_PORT | IN | UInt | Default value = 502: The IP port number of the server to which the client will attempt to connect and ultimately communicate using the TCP/IP protocol. |
| MB\_MODE | IN | USInt | Mode Selection: Assigns the type of request (read, write, or diagnostic). See the Modbus functions table below for details. |
| MB\_DATA\_ADDR | IN | UDInt | Modbus starting Address: Assigns the starting address of the data to be accessed by MB\_CLIENT. See the Modbus functions table below for valid addresses. |
| MB\_DATA\_LEN | IN | UInt | Modbus data Length: Assigns the number of bits or words to be accessed in this request. See the Modbus functions table below for valid lengths |
| MB\_DATA\_PTR | IN\_OUT | Variant | Pointer to the Modbus data register: The register buffers data going to or coming from a Modbus server. The pointer must assign a non-optimized global DB or a M memory address. |
| DONE | OUT | Bool | The DONE bit is TRUE for one scan, after the last request was completed with no error. |
| BUSY | OUT | Bool | - 0 - No MB\_CLIENT operation in progress - 1 - MB\_CLIENT operation in progress |
| ERROR | OUT | Bool | The ERROR bit is TRUE for one scan, after the MB\_CLIENT execution was terminated with an error. The error code value at the STATUS parameter is valid only during the single cycle where ERROR = TRUE. |
| STATUS | OUT | Word | Execution condition code |

## REQ parameter

FALSE = No Modbus communication request

TRUE = Request to communicate with a Modbus TCP server

If no instance of MB\_CLIENT is active and parameter DISCONNECT=0, when REQ=1 a new Modbus request will start. If the connection is not already established then a new connection will be made.

If the same instance of MB\_CLIENT is executed again with DISCONNECT=0 and REQ=1, before the completion of the current request, then no subsequent Modbus transmission will be made. However, as soon as the current request is completed, a new request can be processed if MB\_CLIENT is executed with REQ=1.

When the current MB\_CLIENT communication request is complete, the DONE bit is TRUE for one cycle. The DONE bit can be used as a time gate to sequence multiple MB\_CLIENT requests.

Note:

**Input data consistency during MB\_CLIENT processing**

Once a Modbus client initiates a Modbus operation, all the input states are saved internally and are then compared on each successive call. The comparison is used to determine if this particular call was the originator of the active client request. More than one MB\_CLIENT call can be performed using a common instance DB.

As a result, it is important that the inputs are not changed during the period of time that a MB\_CLIENT operation is actively being processed. If this rule is not followed, then a MB\_CLIENT cannot determine that it is the active instance.

## MB\_MODE and MB\_DATA\_ADDR parameters select the Modbus communication function

MB\_DATA\_ADDR assigns the starting Modbus address of the data to be accessed. The MB\_CLIENT instruction uses a MB\_MODE input rather than a function code input.

The combination of MB\_MODE and MB\_DATA\_ADDR values determine the function code that is used in the actual Modbus message. The following table shows the correspondence between parameter MB\_MODE, Modbus function, and Modbus address range.

Table 3. Modbus functions

| **MB\_MODE** | **Modbus function** | **Data length** | **Operation and data** | **MB\_DATA\_ADDR** |
| --- | --- | --- | --- | --- |
| 0 | 01 | 1 to 2000 | Read output bits:  1 to 2000 bits per request | 1 to 9999 |
| 0 | 02 | 1 to 2000 | Read input bits:  1 to 2000 bits per request | 10001 to 19999 |
| 0 | 03 | 1 to 125 | Read Holding registers:  1 to 125 words per request | 40001 to 49999 or  400001 to 465535 |
| 0 | 04 | 1 to 125 | Read input words:  1 to 125 words per request | 30001 to 39999 |
| 1 | 05 | 1 | Write one output bit:  One bit per request | 1 to 9999 |
| 1 | 06 | 1 | Write one holding register:  1 word per request | 40001 to 49999 or  400001 to 465535 |
| 1 | 15 | 2 to 1968 | Write multiple output bits:  2 to 1968 bits per request | 1 to 9999 |
| 1 | 16 | 2 to 123 | Write multiple holding registers:  2 to 123 words per request | 40001 to 49999 or  400001 to 465535 |
| 2 | 15 | 1 to 1968 | Write one or more output bits:  1 to 1968 bits per request | 1 to 9999 |
| 2 | 16 | 1 to 123 | Write one or more holding registers:  1 to 123 words per request | 40001 to 49999 or  400001 to 465535 |
| 11 | 11 | 0 | Read the server communication status word and event counter. The status word indicates busy (0 – not busy, 0xFFFF - busy). The event counter is incremented for each successful completion of a message.  Both the MB\_DATA\_ADDR and MB\_DATA\_LEN parameters of MB\_CLIENT are ignored for this function. |  |
| 80 | 08 | 1 | Check server status using data diagnostic code 0x0000 (Loopback test – server echoes the request)  1 word per request |  |
| 81 | 08 | 1 | Reset server event counter using data diagnostic code 0x000A  1 word per request |  |
| 3 to 10,  12 to 79,  82 to 255 |  |  | Reserved |  |

Note:

**MB\_DATA\_PTR assigns a buffer to store data read/written to/from a Modbus TCP server**

The data buffer can be in a non-optimized global DB or M memory address.

For a buffer in M memory, use the standard Any Pointer format. This is in the format P#"Bit Address" "Data Type" "Length", an example would be P#M1000.0 WORD 500.

## MB\_DATA\_PTR assigns a communication buffer

- MB\_CLIENT communication functions:

  - Read and write 1-bit data from Modbus server addresses (00001 to 09999)
  - Read 1-bit data from Modbus server addresses (10001 to 19999)
  - Read 16-bit word data from Modbus server addresses (30001 to 39999) and (40001 to 49999)
  - Write 16-bit word data to Modbus server addresses (40001 to 49999)
- Word or bit sized data is transferred to/from the DB or M memory buffer assigned by MB\_DATA\_PTR.
- If a DB is assigned as the buffer by MB\_DATA\_PTR, then you must assign data types to all DB data elements.

  - The 1-bit Bool data type represents one Modbus bit address
  - 16-bit single word data types like WORD, UInt, and Int represent one Modbus word address
  - 32-bit double word data types like DWORD, DInt, and Real represent two Modbus word addresses
- Complex DB elements can be assigned by MB\_DATA\_PTR, such as

  - Standard arrays
  - Named structures where each element is unique.
  - Named complex structures where each element has a unique name and a 16 or 32 bit data type.
- There is no requirement that the MB\_DATA\_PTR data areas be in the same global data block (or M memory area). You can assign one data block for Modbus reads, another data block for Modbus writes, or one data block for each MB\_CLIENT station.

## Multiple client connections

A Modbus TCP client can support concurrent connections up to the maximum number of Open User Communications connections allowed by the PLC. The total number of connections for a PLC, including Modbus TCP Clients and Servers, must not exceed the [maximum number of supported Open User Communications connections](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/sLHuVdWZrv8gmzf1L~x4Ww?section=X0addf1af4d428dcab856741f6adb88fc). The Modbus TCP connections may be shared between Client and/or Server type connections.

Individual client connections must follow these rules:

- Each MB\_CLIENT connection must use a distinct instance DB
- Each MB\_CLIENT connection must specify a unique server IP address
- Each MB\_CLIENT connection must specify a unique connection ID
- Unique IP port numbers may or may not be required depending upon the server configuration

The Connection ID must be unique for each individual connection. This means a single, unique Connection ID must only be used with each individual instance DB. In summary, the instance DB and the Connection ID are paired together and must be unique for every connection.

Table 4. MB\_CLIENT instance data block user accessible static variables

| **Variable** | **Data type** | **Default** | **description** |
| --- | --- | --- | --- |
| Blocked\_Proc\_Timeout | Real | 3.0 | Amount of time (in seconds) to wait upon a blocked Modbus client instance before removing this instance as being ACTIVE. This can occur, for example, when a client request has been issued and then application stops executing the client function before it has completely finished the request. The maximum S7-1200 limit is 55 seconds. |
| MB\_Unit\_ID | Word | 255 | Modbus unit identifier:  A Modbus TCP server is addressed using its IP address. As a result, the MB\_UNIT\_ID parameter is not used for Modbus TCP addressing.  The MB\_UNIT\_ID parameter corresponds to the slave address in the Modbus RTU protocol. If a Modbus TCP server is used for a gateway to a Modbus RTU protocol, the MB\_UNIT\_ID can be used to identify the slave device connected on the serial network. The MB\_UNIT\_ID would be used to forward the request to the correct Modbus RTU slave address.  Some Modbus TCP devices may require the MB\_UNIT\_ID parameter to be initialized within a restricted range of values. |
| RCV\_TIMEOUT | Real | 2.0 | Time in seconds that the MB\_CLIENT waits for a server to respond to a request. |
| Connected | Bool | 0 | Indicates whether the connection to the assigned server is connected or disconnected: 1=connected, 0=disconnected |

Table 5. MB\_CLIENT protocol errors

| **STATUS (W#16#)** | **Response code to Modbus client (B#16#)** | **Modbus protocol errors** |
| --- | --- | --- |
| 8381 | 01 | Function code not supported |
| 8382 | 03 | Data length error |
| 8383 | 02 | Data address error or access outside the bounds of the MB\_HOLD\_REG address area |
| 8384 | 03 | Data value error |
| 8385 | 03 | Data diagnostic code value not supported (function code 08) |

Table 6. MB\_CLIENT execution condition codes 1

| **STATUS (W#16#)** | **MB\_CLIENT parameter errors** |
| --- | --- |
| 7001 | MB\_CLIENT is waiting for a Modbus server response to a connect or disconnect request, on the assigned TCP port. This is only reported for the first execution of a connect or disconnect operation. |
| 7002 | MB\_CLIENT is waiting for a Modbus server response to a connect or disconnect request, for the assigned TCP port. This will be reported for any subsequent executions, while waiting for completion of a connect or disconnect operation. |
| 7003 | A disconnect operation has successfully completed (Only valid for one PLC scan). |
| 80C8 | The server did not respond in the assigned time. MB\_CLIENT must receive a response using the transaction ID that was originally transmitted within the assigned time or this error is returned. Check the connection to the Modbus server device.  This error is only reported after any configured retries (if applicable) have been attempted. |
| 8188 | Invalid mode value |
| 8189 | Invalid data address value |
| 818A | Invalid data length value |
| 818B | Invalid pointer to the DATA\_PTR area. This can be the combination of MB\_DATA\_ADDRESS + MB\_DATA\_LEN. |
| 818C | Pointer to a optimized DATA\_PTR area (must be a non-optimized DB area or M memory area) |
| 8200 | The port is busy processing an existing Modbus request. |
| 8380 | Received Modbus frame is malformed or too few bytes have been received. |
| 8387 | The assigned Connection ID parameter is different from the ID used for previous requests. There can only be a single Connection ID used within each MB\_CLIENT instance DB.  This is also used as an internal error if the Modbus TCP protocol ID received from a server is not 0. |
| 8388 | A Modbus server returned a quantity of data that is different than what was requested. This applies to Modbus functions 15 or 16 only. |

1 In addition to the MB\_CLIENT errors listed above, errors can be returned from the underlying [T block communication instructions (TCON, TDISCON, TSEND, and TRCV](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/PK7AxFUchOqev~QYmER8Jg?section=X6429d5b913b72dbf8463c43b953f4119)).

---

#### MB_SERVER (Communicate using PROFINET as Modbus TCP server)

The "MB\_SERVER" instruction communicates as Modbus TCP server through the PROFINET connector on the S7-1200 CPU. The "MB\_SERVER" instruction processes connection requests of a Modbus TCP client, receives and processes Modbus requests, and sends responses.

To use the instruction, you do not require an additional hardware module.

Warning:

**Risks with access to the process image**

Each Modbus TCP client has read and write access to the process image inputs and outputs, and to the data block or bit memory area defined by the Modbus holding register. Unauthorized read and write operations can change PLC variables into invalid values and disrupt process operations.

To reduce the risk of unauthorized access, restrict access to an IP address of a specific Modbus client. For information on additional industrial security measures that can be implemented, please visit the [Siemens Industrial Cybersecurity site](https://www.siemens.com/global/en/products/automation/topic-areas/industrial-cybersecurity.html).

Disruption of process operations can result in death, severe injury and/or property damage.

Table 1. MB\_SERVER instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"MB\_SERVER\_DB"(    DISCONNECT:=\_bool\_in\_,    CONNECT\_ID:=\_uint\_in\_,    IP\_PORT:=\_uint\_in\_,    NDR=>\_bool\_out\_,    DR=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    MB\_HOLD\_REG:=\_variant\_inout\_);** | MB\_SERVER communicates as a Modbus TCP server through the PROFINET connector on the S7-1200 CPU. No additional communication hardware module is required.  MB\_SERVER can accept a request to connect with Modbus TCP client, receive a Modbus function request, and send a response message. |

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| DISCONNECT | IN | Bool | MB\_SERVER attempts to make a "passive" connection with a partner device. This means that the server is passively listening for a TCP connection request from any requesting IP address.  If DISCONNECT = 0 and a connection does not exist, then a passive connection can be initiated.  If DISCONNECT = 1 and a connection exists, then a disconnect operation is initiated. This allows your program to control when a connection is accepted. Whenever this input is enabled, no other operation will be attempted. |
| CONNECT\_ID | IN | UInt | CONNECT\_ID uniquely identifies each connection within the PLC. Each unique instance of the MB\_CLIENT or MB\_SERVER instruction must contain a unique CONNECT\_ID parameter. |
| IP\_PORT | IN | UInt | Default value = 502: The IP port number that identifies the IP port that will be monitored for a connection request from a Modbus client. |
| MB\_HOLD\_REG | IN\_OUT | Variant | Pointer to the MB\_SERVER Modbus holding register: The holding register must either be a non-optimized global DB or a M memory address. This memory area is used to hold the values a Modbus client is allowed to access using Modbus register functions 3 (read), 6 (write), and 16 (write). |
| NDR | OUT | Bool | New Data Ready: 0 = No new data, 1 = Indicates that new data has been written by a Modbus client |
| DR | OUT | Bool | Data Read: 0 = No data read, 1 = Indicates that data has been read by a Modbus client. |
| ERROR | OUT | Bool | The ERROR bit is TRUE for one scan, after MB\_SERVER execution was terminated with an error. The error code value at the STATUS parameter is valid only during the single cycle where ERROR = TRUE. |
| STATUS | OUT | Word | Execution condition code |

MB\_SERVER allows incoming Modbus function codes (1, 2, 4, 5, and 15) to read or write bits and words directly in the input process image and output process image of the S7-1200 CPU. For data transfer function codes (3, 6, and 16), the MB\_HOLD\_REG parameter must be defined as a data type larger than a byte. The following table shows the mapping of Modbus addresses to the process image in the CPU.

Table 3. Mapping of Modbus addresses to the process image

| **Modbus functions** | | | | | | **S7-1200** | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Codes | Function | Data area | Address range | | | Data area | CPU address |
| 01 | Read bits | Output | 1 | To | 8192 | Output Process Image | Q0.0 to Q1023.7 |
| 02 | Read bits | Input | 10001 | To | 18192 | Input Process Image | I0.0 to I1023.7 |
| 04 | Read words | Input | 30001 | To | 30512 | Input Process Image | IW0 to IW1022 |
| 05 | Write bit | Output | 1 | To | 8192 | Output Process Image | Q0.0 to Q1023.7 |
| 15 | Write bits | Output | 1 | To | 8192 | Output Process Image | Q0.0 to Q1023.7 |

Incoming Modbus message function codes function codes (3, 6, and 16) read or write words in a Modbus holding register which can be an M memory address range or a data block. The type of holding register is specified by the MB\_HOLD\_REG parameter.

Note:

**MB\_HOLD\_REG parameter assignment**

The Modbus Holding Register can be in a non-optimized global DB or an M memory address.

For A Modbus holding register in M memory, use the standard Any Pointer format. This is in the format P#"Bit Address" "Data Type" "Length". An example would be P#M1000.0 WORD 500

The following table shows examples of Modbus address to holding register mapping used for Modbus function codes 03 (read words), 06 (write word), and 16 (write words). The actual upper limit of DB addresses is determined by the maximum work memory limit and M memory limit, for each CPU model.

Table 4. Mapping examples of Modbus address to CPU memory address

| **Modbus Address** | **MB\_HOLD\_REG parameter examples** | | |
| --- | --- | --- | --- |
| **P#M100.0 Word 5** | **P#DB10.DBx0.0 Word 5** | **"Recipe".ingredient** |
| 40001 | MW100 | DB10.DBW0 | "Recipe".ingredient[1] |
| 40002 | MW102 | DB10.DBW2 | "Recipe".ingredient[2] |
| 40003 | MW104 | DB10.DBW4 | "Recipe".ingredient[3] |
| 40004 | MW106 | DB10.DBW6 | "Recipe".ingredient[4] |
| 40005 | MW108 | DB10.DBW8 | "Recipe".ingredient[5] |

## Multiple server connections

Multiple server connections may be created. This permits a single PLC to establish concurrent connections to multiple Modbus TCP clients.

A Modbus TCP server can support concurrent connections up to the maximum number of Open User Communications connections allowed by the PLC. The total number of connections for a PLC, including Modbus TCP Clients and Servers, must not exceed the [maximum number of supported Open User Communications connections](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/sLHuVdWZrv8gmzf1L~x4Ww?section=X0addf1af4d428dcab856741f6adb88fc). The Modbus TCP connections may be shared between Client and/or Server type connections.

Individual server connection must follow these rules:

- Each MB\_SERVER connection must use a distinct instance DB.
- Each MB\_SERVER connection must be established with a unique IP port number. Only 1 connection per port is supported.
- Each MB\_SERVER connection must use a unique connection ID.
- The MB\_SERVER must be called individually for each connection (with its respective instance DB).

The Connection ID must be unique for each individual connection. This means a single, unique Connection ID must only be used with each individual instance DB. In summary, the instance DB and the Connection ID are paired together and must be unique for every connection.

Table 5. Modbus diagnostic function codes

| **MB\_SERVER Modbus diagnostic functions** | | |
| --- | --- | --- |
| Codes | Sub-function | Description |
| 08 | 0x0000 | Return query data echo test: The MB\_SERVER will echo back to a Modbus client a word of data that is received. |
| 08 | 0x000A | Clear communication event counter: The MB\_SEVER will clear out the communication event counter that is used for Modbus function 11. |
| 11 |  | Get communication event counter: The MB\_SERVER uses an internal communication event counter for recording the number of successful Modbus read and write requests that are sent to the Modbus server. The counter does not increment on any Function 8 or Function 11 requests. It is also not incremented on any requests that result in a communication error.  The broadcast function is not available for Modbus TCP, because only one client-server connection exists at any one time. |

## MB\_SERVER variables

This table shows the public static variables stored in the MB\_SERVER instance data block that can be used in your program

Table 6. MB\_SERVER public static variables

| **Variable** | **Data type** | **Default value** | **Description** |
| --- | --- | --- | --- |
| HR\_Start\_Offset | Word | 0 | Assigns the starting address of the Modbus Holding register |
| Request\_Count | Word | 0 | The number of all requests received by this server. |
| Server\_Message\_Count | Word | 0 | The number of requests received for this specific server. |
| Xmt\_Rcv\_Count | Word | 0 | The number of transmissions or receptions that have encountered an error. Also, incremented if a message is received that is an invalid Modbus message. |
| Exception\_Count | Word | 0 | Modbus specific errors that require a returned exception |
| Success\_Count | Word | 0 | The number of requests received for this specific server that has no protocol errors. |
| Connected | Bool | 0 | Indicates whether the connection to the assigned client is connected or disconnected: 1=connected, 0=disconnected |

Your program can write values to the HR\_Start\_Offset and control Modbus server operations. The other variables can be read to monitor Modbus status.

## HR\_Start\_Offset

Modbus holding register addresses begin at 40001. These addresses correspond to the beginning PLC memory address of the holding register. However, you can configure the "HR\_Start\_Offset" variable to start the beginning Modbus holding register address at another value instead of 40001.

For example, if the holding register is configured to start at MW100 and is 100 words long. An offset of 20 specifies a beginning holding register address of 40021 instead of 40001. Any address below 40021 and above 40119 will result in an addressing error.

Table 7. Example of Modbus holding register addressing

| **HR\_Start\_Offset** | **Address** | **Minimum** | **Maximum** |
| --- | --- | --- | --- |
| 0 | Modbus address (Word) | 40001 | 40099 |
| S7-1200 address | MW100 | MW298 |
| 20 | Modbus address (Word) | 40021 | 40119 |
| S7-1200 address | MW100 | MW298 |

HR\_Start\_Offset is a word value that specifies the starting address of the Modbus holding register and is stored in the MB\_SERVER instance data block. You can set this public static variable value by using the parameter helper drop-list, after MB\_SERVER is placed in your program.

For example, after MB\_SERVER is placed in a LAD network, you can go to a previous network and assign the HR\_Start\_Offset value. The value must be assigned prior to execution of MB\_SERVER.

|  |  |
| --- | --- |
|  | Entering a Modbus server  variable using the default DB name:   1. Set the cursor in the parameter field and type an m character. 2. Select "MB\_SERVER\_DB" from the drop-list of DB names. 3. Select "MB\_SERVER\_DB.HR\_Start\_Offset" from the drop-list of DB variables. |
|  |
|  |

Table 8. MB\_SERVER execution condition codes 1

| **STATUS (W#16#)** | **Response code to Modbus server (B#16#)** | **Modbus protocol errors** |
| --- | --- | --- |
| 7001 |  | MB\_SERVER is waiting for a Modbus client to connect to the assigned TCP port. This code is reported on the first execution of a connect or disconnect operation. |
| 7002 |  | MB\_SERVER is waiting for a Modbus client to connect to the assigned TCP port. This code is reported for any subsequent executions, while waiting for completion of a connect or disconnect operation. |
| 7003 |  | A disconnect operation has successfully completed (Only valid for one PLC scan). |
| 8187 |  | Invalid pointer to MB\_HOLD\_REG: area is too small |
| 818C |  | Pointer to an optimized MB\_HOLD\_REG area (must be a non-optimized DB area or M memory area) or Blocked process timeout exceeds the limit of 55 seconds. (S7-1200 specific) |
| 8381 | 01 | Function code not supported |
| 8382 | 03 | Data length error |
| 8383 | 02 | Data address error or access outside the bounds of the MB\_HOLD\_REG address area |
| 8384 | 03 | Data value error |
| 8385 | 03 | Data diagnostic code value not supported (function code 08) |

1 In addition to the MB\_SERVER errors listed above, errors can be returned from the underlying [T block communication instructions (TCON, TDISCON, TSEND, and TRCV](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/PK7AxFUchOqev~QYmER8Jg?section=X6429d5b913b72dbf8463c43b953f4119)).

---

### Legacy Modbus TCP examples


---

#### Example: Legacy MB_SERVER Multiple TCP connections

You can have multiple Modbus TCP server connections. To accomplish this, MB\_SERVER must be independently executed for each connection. Each connection must use an independent instance DB, connection ID, and IP port. The S7-1200 allows only one connection per IP port.

For best performance, MB\_SERVER should be executed every program cycle, for each connection.

**Network 1:** Connection #1 with independent IP\_PORT, connection ID, and instance DB

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/Me2osyLSw1BKSXQVKiDMuA-VBkTPlmjVZAl17lebjV9hA/content?v=cecf071e9f0533cb)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/Me2osyLSw1BKSXQVKiDMuA-VBkTPlmjVZAl17lebjV9hA)

**Network 2:** Connection #2 with independent IP\_PORT, connection ID, and instance DB

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/AG2AOrz_kFYdT1k61vkCyA-VBkTPlmjVZAl17lebjV9hA/resized-content?v=fe9a64840d15da0a)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/AG2AOrz_kFYdT1k61vkCyA-VBkTPlmjVZAl17lebjV9hA)

---

#### Example: Legacy MB_CLIENT 1: Multiple requests with common TCP connection

Multiple Modbus client requests can be sent over the same connection. To accomplish this, use the same instance DB, connection ID, and port number.

Only 1 client can be active at any given time. Once a client completes its execution, the next client begins execution. Your program is responsible for the order of execution.

The example shows both clients writing to the same memory area. Also, a returned error is captured which is optional.

**Network 1:** Modbus function 1 - Read 16 output image bits

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/ay4eWdqdxjwQw8oOiEDYjw-VBkTPlmjVZAl17lebjV9hA/content?v=dee482d611530fb1)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/ay4eWdqdxjwQw8oOiEDYjw-VBkTPlmjVZAl17lebjV9hA)

**Network 2:** Modbus function 2 - Read 32 input image bits

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/pRSfSrJlOoyg8UpR9dYJKA-VBkTPlmjVZAl17lebjV9hA/content?v=7468f0eb90b7a6fb)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/pRSfSrJlOoyg8UpR9dYJKA-VBkTPlmjVZAl17lebjV9hA)

---

#### Example: Legacy MB_CLIENT 2: Multiple requests with different TCP connections

Modbus client requests can be sent over different connections. To accomplish this, different instance DBs, IP addresses, and connection IDs must be used.

The port number must be different if the connections are established to the same Modbus server. If the connections are on different servers, there is no port number restriction.

The example shows both clients writing to the same memory area. Also, a returned error is captured which is optional.

**Network 1:**

Modbus function 4 - Read input words (in S7-1200 memory)

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/m9el8B0Nlbt7hyP0tl2jvw-VBkTPlmjVZAl17lebjV9hA/content?v=c89662f1def6f797)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/m9el8B0Nlbt7hyP0tl2jvw-VBkTPlmjVZAl17lebjV9hA)

**Network 2:** Modbus function 3 - Read holding register words from a Modbus TCP server

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/1e2St0DtfL~1d4~S71T2bg-VBkTPlmjVZAl17lebjV9hA/content?v=8dedac51366d0312)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/1e2St0DtfL~1d4~S71T2bg-VBkTPlmjVZAl17lebjV9hA)

---

#### Example: Legacy MB_CLIENT 3: Output image write request

This example shows a Modbus client request to write the S7-1200 output image.

**Network 1:** Modbus function 15 - Write S7-1200 output image bits

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/pT6~gdDvwJ9JnJATPbFNQA-VBkTPlmjVZAl17lebjV9hA/content?v=937b9c7cf31026f7)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/pT6~gdDvwJ9JnJATPbFNQA-VBkTPlmjVZAl17lebjV9hA)

---

#### Example: Legacy MB_CLIENT 4: Coordinating multiple requests

You must ensure that each individual Modbus TCP request finishes execution. This coordination must be provided by your program. The example below shows how the outputs of the first and second client requests can be used to coordinate execution.

The example shows both clients writing to the same memory area. Also, a returned error is captured which is optional.

**Network 1:** Modbus function 3 - Read holding register words

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/Uw_GY~xaZ1vCM815pkAdEA-VBkTPlmjVZAl17lebjV9hA/content?v=4438b06fc5a6245e)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/Uw_GY~xaZ1vCM815pkAdEA-VBkTPlmjVZAl17lebjV9hA)

**Network 2:** Modbus function 3 - Read holding register words

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/pSlyn7jzbllnb1CfASLhdA-VBkTPlmjVZAl17lebjV9hA/content?v=1adbdfaa8265cc31)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/pSlyn7jzbllnb1CfASLhdA-VBkTPlmjVZAl17lebjV9hA)

---

## Legacy Modbus RTU communication (CM/CB 1241 only)


---

### Overview

Prior to the release of STEP 7 V13 SP1 and the S7-1200 V4.1 CPUs, the Modbus RTU communication instructions existed with different names, and in some cases, slightly different interfaces. The general concepts apply to both sets of instructions. Refer to the individual legacy Modbus RTU instructions for programming information.

STEP 7 provides different versions of the Modbus RTU instructions. For information on instruction versions, refer to [Use Instruction versions](https://support.industry.siemens.com/cs/ww/en/view/109798671/113722878475) in the STEP 7 Information System.

---

### Legacy Modbus RTU instructions


---

#### MB_COMM_LOAD (Configure port on the PtP module for Modbus RTU)

Table 1. MB\_COMM\_LOAD instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"MB\_COMM\_LOAD\_DB"(    REQ:=\_bool\_in,    PORT:=\_uint\_in\_,    BAUD:=\_udint\_in\_,    PARITY:=\_uint\_in\_,    FLOW\_CTRL:=\_uint\_in\_,    RTS\_ON\_DLY:=\_uint\_in\_,    RTS\_OFF\_DLY:=\_uint\_in\_,    RESP\_TO:=\_uint\_in\_,    DONE=>\_bool\_out,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    MB\_DB:=\_fbtref\_inout\_);** | The MB\_COMM\_LOAD instruction configures a PtP port for Modbus RTU protocol communications. Modbus port hardware options: Install up to three CMs (RS485 or RS232), plus one CB (R4845). An instance data block is assigned automatically when you place the MB\_COMM\_LOAD instruction in your program. |

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | A low to high (positive edge) signal starts the operation.  (Version 2.0 only) |
| PORT | IN | Port | After you install and configure a CM or CB communication device, the port identifier appears in the parameter helper drop-list available at the PORT box connection. The assigned CM or CB port value is the device configuration property "hardware identifier". The port symbolic name is assigned in the "System constants" tab of the PLC tag table. |
| BAUD | IN | UDInt | Baud rate selection:  300, 600, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 76800, 115200, all other values are invalid |
| PARITY | IN | UInt | Parity selection:   - 0 – None - 1 – Odd - 2 – Even |
| FLOW\_CTRL 1 | IN | UInt | Flow control selection:   - 0 – (default) no flow control - 1 – Hardware flow control with RTS always ON (does not apply to RS485 ports) - 2 – Hardware flow control with RTS switched |
| RTS\_ON\_DLY 1 | IN | UInt | RTS ON delay selection:   - 0 – (default) No delay from RTS active until the first character of the message is transmitted - 1 to 65535 – Delay in milliseconds from RTS active until the first character of the message is transmitted (does not apply to RS485 ports). RTS delays shall be applied independent of the FLOW\_CTRL selection. |
| RTS\_OFF\_DLY 1 | IN | UInt | RTS OFF delay selection:   - 0 – (default) No delay from the last character transmitted until RTS goes inactive - 1 to 65535 – Delay in milliseconds from the last character transmitted until RTS goes inactive (does not apply to RS485 ports). RTS delays shall be applied independent of the FLOW\_CTRL selection. |
| RESP\_TO 1 | IN | UInt | Response timeout:  Time in milliseconds allowed by MB\_MASTER for the slave to respond. If the slave does not respond in this time period, MB\_MASTER will retry the request or terminate the request with an error when the specified number of retries has been sent.  5 ms to 65535 ms (default value = 1000 ms). |
| MB\_DB | IN | Variant | A reference to the instance data block used by the MB\_MASTER or MB\_SLAVE instructions. After MB\_SLAVE or MB\_MASTER is placed in your program, the DB identifier appears in the parameter helper drop-list available at the MB\_DB box connection. |
| DONE | OUT | Bool | The DONE bit is TRUE for one scan, after the last request was completed with no error. (Version 2.0 only) |
| ERROR | OUT | Bool | The ERROR bit is TRUE for one scan, after the last request was terminated with an error. The error code value at the STATUS parameter is valid only during the single scan where ERROR = TRUE. |
| STATUS | OUT | Word | Execution condition code |

1 Optional parameters for MB\_COMM\_LOAD (V 2.x or later). Click the arrow at the bottom of a LAD/FBD box to expand the box and include these parameters.

MB\_COMM\_LOAD is executed to configure a port for the Modbus RTU protocol. Once a port is configured for the Modbus RTU protocol, it can only be used by either the MB\_MASTER or MB\_SLAVE instructions.

One execution of MB\_COMM\_LOAD must be used to configure each communication port that is used for Modbus communication. Assign a unique MB\_COMM\_LOAD instance DB for each port that you use. You can install up to three communication modules (RS232 or RS485) and one communication board (RS485) in the CPU. Call MB\_COMM\_LOAD from a startup OB and execute it one time or use the [first scan system flag](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/57RJkWqlv2cHgK3TNbVEaA?section=X24485c8cb365163875682d239602aa4b) to initiate the call to execute it one time. Only execute MB\_COMM\_LOAD again if communication parameters like baud rate or parity must change.

An instance data block is assigned for MB\_MASTER or MB\_SLAVE when you place these instructions in your program. This instance data block is referenced when you specify the MB\_DB parameter for the MB\_COMM\_LOAD instruction.

## MB\_COMM\_LOAD data block variables

The following table shows the public static variables stored in the instance DB for the MB\_COMM\_LOAD that can be used in your program.

Table 3. Static variables in the instance DB

| **Variable** | **Data type** | **Description** |
| --- | --- | --- |
| ICHAR\_GAP | UInt | Delay for Inter-character gap between characters. This parameter is specified in milliseconds and is used to increase the expected amount of time between received characters. The corresponding number of bit times for this parameter is added to the Modbus default of 35 bit times (3.5 character times). |
| RETRIES | UInt | Number of retries that the master will attempt before returning the no response error code 0x80C8. |
| STOP\_BITS | USInt | Number of stop bits used in framing each character. Valid values are 1 and 2. |

Table 4. MB\_COMM\_LOAD execution condition codes 1

| **STATUS (W#16#)** | **Description** |
| --- | --- |
| 0000 | No error |
| 8180 | Invalid port ID value (wrong port/hardware identifier for communication module) |
| 8181 | Invalid baud rate value |
| 8182 | Invalid parity value |
| 8183 | Invalid flow control value |
| 8184 | Invalid response timeout value (response timeout less than the 5 ms minimum) |
| 8185 | MB\_DB parameter is not an instance data block of a MB\_MASTER or MB\_SLAVE instruction. |

1 In addition to the MB\_COMM\_LOAD errors listed above, errors can be returned from the underlying PtP communication instructions.

---

#### MB_MASTER (Communicate using the PtP port as Modbus RTU master)

Table 1. MB\_MASTER instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"MB\_MASTER\_DB"(    REQ:=\_bool\_in\_,    MB\_ADDR:=\_uint\_in\_,    MODE:=\_usint\_in\_,    DATA\_ADDR:=\_udint\_in\_,    DATA\_LEN:=\_uint\_in\_,    DONE=>\_bool\_out\_,    BUSY=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    DATA\_PTR:=\_variant\_inout\_);** | The MB\_MASTER instruction communicates as a Modbus master using a port that was configured by a previous execution of the MB\_COMM\_LOAD instruction. An instance data block is assigned automatically when you place the MB\_MASTER instruction in your program. This MB\_MASTER instance data block is used when you specify the MB\_DB parameter for the MB\_COMM\_LOAD instruction. |

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| REQ | IN | Bool | 0=No request  1= Request to transmit data to Modbus slave |
| MB\_ADDR | IN | V1.0: USInt  V2.0: UInt | Modbus RTU station address:  Standard addressing range (1 to 247)  Extended addressing range (1 to 65535)  The value of 0 is reserved for broadcasting a message to all Modbus slaves. Modbus function codes 05, 06, 15 and 16 are the only function codes supported for broadcast. |
| MODE | IN | USInt | Mode Selection: Specifies the type of request (read, write, or diagnostic). See the Modbus functions table below for details. |
| DATA\_ADDR | IN | UDInt | Starting Address in the slave: Specifies the starting address of the data to be accessed in the Modbus slave. See the Modbus functions table below for valid addresses. |
| DATA\_LEN | IN | UInt | Data Length: Specifies the number of bits or words to be accessed in this request. See the Modbus functions table below for valid lengths. |
| DATA\_PTR | IN | Variant | Data Pointer: Points to the M or DB address (non-optimized DB type) for the data being written or read. |
| DONE | OUT | Bool | The DONE bit is TRUE for one scan, after the last request was completed with no error. |
| BUSY | OUT | Bool | - 0 – No MB\_MASTER operation in progress - 1 – MB\_MASTER operation in progress |
| ERROR | OUT | Bool | The ERROR bit is TRUE for one scan, after the last request was terminated with an error. The error code value at the STATUS parameter is valid only during the single scan where ERROR = TRUE. |
| STATUS | OUT | Word | Execution condition code |

## Modbus master communication rules

- MB\_COMM\_LOAD must be executed to configure a port before a MB\_MASTER instruction can communicate with that port.
- If a port is to be used to initiate Modbus master requests, that port should not be used by MB\_SLAVE. One or more instances of MB\_MASTER execution can be used with that port, but all MB\_MASTER execution must use the same MB\_MASTER instance DB for that port.
- The Modbus instructions do not use communication interrupt events to control the communication process. Your program must poll the MB\_MASTER instruction for transmit and receive complete conditions.
- Call all MB\_MASTER execution for a given port from a program cycle OB. Modbus master instructions may execute in only one of the program cycle or cyclic/time delay execution levels. They must not execute in both execution priority levels. Pre-emption of a Modbus Master instruction by another Modbus master instruction in a higher priority execution priority level will result in improper operation. Modbus master instructions must not execute in the startup, diagnostic or time error execution priority levels.
- Once a master instruction initiates a transmission, this instance must be continually executed with the EN input enabled until a DONE=1 state or ERROR=1 state is returned. A particular MB\_MASTER instance is considered active until one of these two events occurs. While the original instance is active, any call to any other instance with the REQ input enabled will result in an error. If the continuous execution of the original instance stops, the request state remains active for a period of time specified by the static variable Blocked\_Proc\_Timeout. Once this period of time expires, the next master instruction called with an enabled REQ input will become the active instance. This prevents a single Modbus master instance from monopolizing or locking access to a port. If the original active instance is not enabled within the period of time specified by the static variable "Blocked\_Proc\_Timeout", then the next execution by this instance (with REQ not set) will clear the active state. If (REQ is set), then this execution initiates a new master request as if no other instance was active.

## REQ parameter

0 = No request; 1 = Request to transmit data to Modbus Slave

You may control this input either through the use of a level or edge triggered contact. Whenever this input is enabled, a state machine is started to ensure that no other MB\_MASTER using the same instance DB is allowed to issue a request, until the current request is completed. All other input states are captured and held internally for the current request, until the response is received or an error detected.

If the same instance of MB\_MASTER is executed again with REQ input = 1 before the completion of the current request, then no subsequent transmissions are made. However, when the request is completed, a new request is issued whenever MB\_MASTER is executed again with REQ input = 1.

## DATA\_ADDR and MODE parameters select the Modbus function type

DATA\_ADDR (starting Modbus address in the slave): Specifies the starting address of the data to be accessed in the Modbus slave.

The MB\_MASTER instruction uses a MODE input rather than a Function Code input. The combination of MODE and Modbus address determine the Function Code that is used in the actual Modbus message. The following table shows the correspondence between parameter MODE, Modbus function code, and Modbus address range.

Table 3. Modbus functions

| **MODE** | **Modbus Function** | **Data length** | **Operation and data** | **Modbus Address** |
| --- | --- | --- | --- | --- |
| 0 | 01 | 1 to 2000  1 to 1992 1 | Read output bits:  1 to (1992 or 2000) bits per request | 1 to 9999 |
| 0 | 02 | 1 to 2000  1 to 1992 1 | Read input bits:  1 to (1992 or 2000) bits per request | 10001 to 19999 |
| 0 | 03 | 1 to 125  1 to 124 1 | Read Holding registers:  1 to (124 or 125) words per request | 40001 to 49999 or  400001 to 465535 |
| 0 | 04 | 1 to 125  1 to 124 1 | Read input words:  1 to (124 or 125) words per request | 30001 to 39999 |
| 1 | 05 | 1 | Write one output bit:  One bit per request | 1 to 9999 |
| 1 | 06 | 1 | Write one holding register:  1 word per request | 40001 to 49999 or  400001 to 465535 |
| 1 | 15 | 2 to 1968  2 to 1960 1 | Write multiple output bits:  2 to (1960 or 1968) bits per request | 1 to 9999 |
| 1 | 16 | 2 to 123  2 to 122 1 | Write multiple holding registers:  2 to (122 or 123) words per request | 40001 to 49999 or  400001 to 465535 |
| 2 | 15 | 1 to 1968  2 to 1960 1 | Write one or more output bits:  1 to (1960 or 1968) bits per request | 1 to 9999 |
| 2 | 16 | 1 to 123  1 to 122 1 | Write one or more holding registers:  1 to (122 or 123) words per request | 40001 to 49999 or  400001 to 465535 |
| 11 | 11 | 0 | Read the slave communication status word and event counter. The status word indicates busy (0 – not busy, 0xFFFF - busy). The event counter is incremented for each successful completion of a message.  Both the DATA\_ADDR and DATA\_LEN operands of MB\_MASTER are ignored for this function. |  |
| 80 | 08 | 1 | Check slave status using data diagnostic code 0x0000 (Loopback test – slave echoes the request)  1 word per request |  |
| 81 | 08 | 1 | Reset slave event counter using data diagnostic code 0x000A  1 word per request |  |
| 3 to 10,  12 to 79,  82 to 255 |  |  | Reserved |  |

1For "Extended Addressing" mode the maximum data lengths are reduced by 1 byte or 1 word depending upon the data type used by the function.

## DATA\_PTR parameter

The DATA\_PTR parameter points to the DB or M address that is written to or read from. If you use a data block, then you must create a global data block that provides data storage for reads and writes to Modbus slaves.

Note:

**The DATA\_PTR data block type must allow direct addressing**

The data block must allow both direct (absolute) and symbolic addressing. When you create the data block the "Standard" access attribute must be selected.

## Data block structures for the DATA\_PTR parameter

- These data types are valid for **word reads** of Modbus addresses 30001 to 39999, 40001 to 49999, and 400001 to 465536 and also for **word writes** to Modbus addresses 40001 to 49999 and 400001 to 465536.

  - Standard array of WORD, UINT, or INT data types
  - Named WORD, UINT, or INT structure where each element has a unique name and 16 bit data type.
  - Named complex structure where each element has a unique name and a 16 or 32 bit data type.
- For **bit reads** and writes of Modbus addresses 00001 to 09999 and bit reads of 10001 to 19999.

  - Standard array of Boolean data types.
  - Named Boolean structure of uniquely named Boolean variables.
- Although not required, it is recommended that each MB\_MASTER instruction have its own separate memory area. The reason for this recommendation is that there is a greater possibility of data corruption if multiple MB\_MASTER instructions are reading and writing to the same memory area.
- There is no requirement that the DATA\_PTR data areas be in the same global data block. You can create one data block with multiple areas for Modbus reads, one data block for Modbus writes, or one data block for each slave station.

## Modbus master data block variables

The following table shows the public static variables stored in the instance DB for MB\_MASTER that can be used in your program.

Table 4. Static variables in the instance DB

| **Variable** | **Data type** | **Initial value** | **Description** |
| --- | --- | --- | --- |
| Blocked\_Proc\_Timeout | Real | 3.0 | Amount of time (in seconds) to wait for a blocked Modbus Master instance before removing this instance as being ACTIVE. This can occur, for example, when a Master request has been issued and then the program stops calling the Master function before it has completely finished the request. The time value must be greater than 0 and less than 55 seconds, or an error occurs. The default value is .5 seconds. |
| Extended\_Addressing | Bool | False | Configures single or double-byte slave addressing. The default value = 0.  (0=single byte address, 1=double-byte address) |

Your program can write values to the Blocked\_Proc\_Timeout and Extended\_Addressing variables to control Modbus master operations. [See the MB\_SLAVE topic description of HR\_Start\_Offset and Extended\_Addressing for an example of how to use these variables in the program editor and details about Modbus extended addressing](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/pO95c2rzk_clBfXYvsVaxQ?section=X3bab1d6ca864b359a290f8fbb04aab2c).

## Condition codes

Table 5. MB\_MASTER execution condition codes (communication and configuration errors) 1

| **STATUS (W#16#)** | **Description** |
| --- | --- |
| 0000 | No error |
| 80C8 | Slave timeout. Check baud rate, parity, and wiring of slave. |
| 80D1 | The receiver issued a flow control request to suspend an active transmission and never re-enabled the transmission during the specified wait time.  This error is also generated during hardware flow control when the receiver does not assert CTS within the specified wait time. |
| 80D2 | The transmit request was aborted because no DSR signal is received from the DCE. |
| 80E0 | The message was terminated because the receive buffer is full. |
| 80E1 | The message was terminated as a result of a parity error. |
| 80E2 | The message was terminated as a result of a framing error. |
| 80E3 | The message was terminated as a result of an overrun error. |
| 80E4 | The message was terminated as a result of the specified length exceeding the total buffer size. |
| 8180 | Invalid port ID value or error with MB\_COMM\_LOAD instruction |
| 8186 | Invalid Modbus station address |
| 8188 | Invalid Mode specified for broadcast request |
| 8189 | Invalid Data Address value |
| 818A | Invalid Data Length value |
| 818B | Invalid pointer to the local data source/destination: Size not correct |
| 818C | Invalid pointer for DATA\_PTR or invalid Blocked\_Proc\_Timeout: The data area must be a DB (that allows both symbolic and direct access) or M memory. |
| 8200 | Port is busy processing a transmit request. |

Table 6. MB\_MASTER execution condition codes (Modbus protocol errors) 1

| **STATUS (W#16#)** | **Response code from slave** | **Modbus protocol errors** |
| --- | --- | --- |
| 8380 | - | CRC error |
| 8381 | 01 | Function code not supported |
| 8382 | 03 | Data length error |
| 8383 | 02 | Data address error or address outside the valid range of the DATA\_PTR area |
| 8384 | Greater than 03 | Data value error |
| 8385 | 03 | Data diagnostic code value not supported (function code 08) |
| 8386 | - | Function code in the response does not match the code in the request. |
| 8387 | - | Wrong slave responded |
| 8388 | - | The slave response to a write request is incorrect. The write request returned by the slave does not match what the master actually sent. |

1 In addition to the MB\_MASTER errors listed above, errors can be returned from the underlying PtP communication instructions.

---

#### MB_SLAVE (Communicate using the PtP port as Modbus RTU slave)

Table 1. MB\_SLAVE instruction

| **LAD / FBD** | **SCL** | **Description** |
| --- | --- | --- |
|  | **"MB\_SLAVE\_DB"(    MB\_ADDR:=\_uint\_in\_,    NDR=>\_bool\_out\_,    DR=>\_bool\_out\_,    ERROR=>\_bool\_out\_,    STATUS=>\_word\_out\_,    MB\_HOLD\_REG:=\_variant\_inout\_);** | The MB\_SLAVE instruction allows your program to communicate as a Modbus slave through a PtP port on the CM (RS485 or RS232) and CB (RS485). When a remote Modbus RTU master issues a request, your user program responds to the request by MB\_SLAVE execution. STEP 7 automatically creates an instance DB when you insert the instruction. Use this MB\_SLAVE\_DB name when you specify the MB\_DB parameter for the MB\_COMM\_LOAD instruction. |

Table 2. Data types for the parameters

| **Parameter and type** | | **Data type** | **Description** |
| --- | --- | --- | --- |
| MB\_ADDR | IN | V1.0: USInt  V2.0: UInt | The station address of the Modbus slave:  Standard addressing range (1 to 247)  Extended addressing range (0 to 65535) |
| MB\_HOLD\_REG | IN | Variant | Pointer to the Modbus Holding Register DB: The Modbus holding register can be M memory or a data block. |
| NDR | OUT | Bool | New Data Ready:   - 0 – No new data - 1 – Indicates that new data has been written by the Modbus master |
| DR | OUT | Bool | Data Read:   - 0 – No data read - 1 – Indicates that data has been read by the Modbus master |
| ERROR | OUT | Bool | The ERROR bit is TRUE for one scan, after the last request was terminated with an error. If execution is terminated with an error, then the error code value at the STATUS parameter is valid only during the single scan where ERROR = TRUE. |
| STATUS | OUT | Word | Execution error code |

Modbus communication function codes (1, 2, 4, 5, and 15) can read and write bits and words directly in the input process image and output process image of the CPU. For these function codes, the MB\_HOLD\_REG parameter must be defined as a data type larger than a byte. The following table shows the example mapping of Modbus addresses to the process image in the CPU.

Table 3. Mapping of Modbus addresses to the process image

| **Modbus functions** | | | | | | **S7-1200** | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Codes | Function | Data area | Address range | | | Data area | CPU address |
| 01 | Read bits | Output | 1 | to | 8192 | Output Process Image | Q0.0 to Q1023.7 |
| 02 | Read bits | Input | 10001 | to | 18192 | Input Process Image | I0.0 to I1023.7 |
| 04 | Read words | Input | 30001 | to | 30512 | Input Process Image | IW0 to IW1022 |
| 05 | Write bit | Output | 1 | to | 8192 | Output Process Image | Q0.0 to Q1023.7 |
| 15 | Write bits | Output | 1 | to | 8192 | Output Process Image | Q0.0 to Q1023.7 |

Modbus communication function codes (3, 6, 16) use a Modbus holding register which can be an M memory address range or a data block. The type of holding register is specified by the MB\_HOLD\_REG parameter on the MB\_SLAVE instruction.

Note:

**MB\_HOLD\_REG data block type**

A Modbus holding register data block must allow both direct (absolute) and symbolic addressing. When you create the data block the "Standard" access attribute must be selected.

The following table shows examples of Modbus address to holding register mapping that is used for Modbus function codes 03 (read words), 06 (write word), and 16 (write words). The actual upper limit of DB addresses is determined by the maximum work memory limit and M memory limit, for each CPU model.

Table 4. Mapping of Modbus addresses to CPU memory

| **Modbus Master Address** | **MB\_HOLD\_REG parameter examples** | | | | |
| --- | --- | --- | --- | --- | --- |
| **MW100** | **DB10.DBw0** | **MW120** | **DB10.DBW50** | **"Recipe".ingredient** |
| 40001 | MW100 | DB10.DBW0 | MW120 | DB10.DBW50 | "Recipe".ingredient[1] |
| 40002 | MW102 | DB10.DBW2 | MW122 | DB10.DBW52 | "Recipe".ingredient[2] |
| 40003 | MW104 | DB10.DBW4 | MW124 | DB10.DBW54 | "Recipe".ingredient[3] |
| 40004 | MW106 | DB10.DBW6 | MW126 | DB10.DBW56 | "Recipe".ingredient[4] |
| 40005 | MW108 | DB10.DBW8 | MW128 | DB10.DBW58 | "Recipe".ingredient[5] |

Table 5. Diagnostic functions

| **S7-1200 MB\_SLAVE Modbus diagnostic functions** | | |
| --- | --- | --- |
| Codes | Sub-function | Description |
| 08 | 0000H | Return query data echo test: The MB\_SLAVE will echo back to a Modbus master a word of data that is received. |
| 08 | 000AH | Clear communication event counter: The MB\_SLAVE will clear out the communication event counter that is used for Modbus function 11. |
| 11 |  | Get communication event counter: The MB\_SLAVE uses an internal communication event counter for recording the number of successful Modbus read and write requests that are sent to the Modbus slave. The counter does not increment on any Function 8, Function 11, or broadcast requests. It is also not incremented on any requests that result in a communication error (for example, parity or CRC errors). |

The MB\_SLAVE instruction supports broadcast write requests from any Modbus master as long as the request is for accessing valid addresses. MB\_SLAVE will produce error code 0x8188 for function codes not supported in broadcast.

## Modbus slave communication rules

- MB\_COMM\_LOAD must be executed to configure a port, before a MB\_SLAVE instruction can communicate through that port.
- If a port is to respond as a slave to a Modbus master, then do not program that port with the MB\_MASTER instruction.
- Only one instance of MB\_SLAVE can be used with a given port, otherwise erratic behavior may occur.
- The Modbus instructions do not use communication interrupt events to control the communication process. Your program must control the communication process by polling the MB\_SLAVE instruction for transmit and receive complete conditions.
- The MB\_SLAVE instruction must execute periodically at a rate that allows it to make a timely response to incoming requests from a Modbus master. It is recommended that you execute MB\_SLAVE every scan from a program cycle OB. Executing MB\_SLAVE from a cyclic interrupt OB is possible, but is not recommended because of the potential for excessive time delays in the interrupt routine to temporarily block the execution of other interrupt routines.

## Modbus signal timing

MB\_SLAVE must be executed periodically to receive each request from the Modbus master and then respond as required. The frequency of execution for MB\_SLAVE is dependent upon the response timeout period of the Modbus master. This is illustrated in the following diagram.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/EOiTFxYH2x0ndWDRRXpI2g-VBkTPlmjVZAl17lebjV9hA/resized-content?v=07064a1e6de14b01)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/EOiTFxYH2x0ndWDRRXpI2g-VBkTPlmjVZAl17lebjV9hA)

The response timeout period RESP\_TO is the amount of time a Modbus master waits for the start of a response from a Modbus slave. This time period is not defined by the Modbus protocol, but is a parameter of each Modbus master. The frequency of execution (the time between one execution and the next execution) of MB\_SLAVE must be based on the particular parameters of your Modbus master. At a minimum, you should execute MB\_SLAVE twice within the response timeout period of the Modbus master.

## Modbus slave variables

This table shows the public static variables stored in the MB\_SLAVE instance data block that can be used in your program

Table 6. Modbus slave variables

| **Variable** | **Data type** | **Description** |
| --- | --- | --- |
| Request\_Count | Word | The number of all requests received by this slave |
| Slave\_Message\_Count | Word | The number of requests received for this specific slave |
| Bad\_CRC\_Count | Word | The number of requests received that have a CRC error |
| Broadcast\_Count | Word | The number of broadcast requests received |
| Exception\_Count | Word | Modbus specific errors that require a returned exception |
| Success\_Count | Word | The number of requests received for this specific slave that have no protocol errors |
| HR\_Start\_Offset | Word | Specifies the starting address of the Modbus Holding register (default = 0) |
| Extended\_Addressing | Bool | Configures single or double-byte slave addressing  (0=single byte address, 1=double-byte address, default = 0) |

Your program can write values to the HR\_Start\_Offset and Extended\_Addressing variables and control Modbus slave operations. The other variables can be read to monitor Modbus status.

## HR\_Start\_Offset

Modbus holding register addresses begin at 40001 or 400001. These addresses correspond to the beginning PLC memory address of the holding register. However, you can configure the "HR\_Start\_Offset" variable to start the beginning Modbus holding register address at another value instead of 40001 or 400001.

For example, if the holding register is configured to start at MW100 and is 100 words long. An offset of 20 specifies a beginning holding register address of 40021 instead of 40001. Any address below 40021 and above 400119 will result in an addressing error.

Table 7. Example of Modbus holding register addressing

| **HR\_Start\_Offset** | **Address** | **Minimum** | **Maximum** |
| --- | --- | --- | --- |
| 0 | Modbus address (Word) | 40001 | 40099 |
| S7-1200 address | MW100 | MW298 |
| 20 | Modbus address (Word) | 40021 | 40119 |
| S7-1200 address | MW100 | MW298 |

HR\_Start\_Offset is a word value that specifies the starting address of the Modbus holding register and is stored in the MB\_SLAVE instance data block. You can set this public static variable value by using the parameter helper drop-list, after MB\_SLAVE is placed in your program.

For example, after MB\_SLAVE is placed in a LAD network, you can go to a previous network and assign the HR\_Start\_Offset value. The value must be assigned prior to execution of MB\_SLAVE.

|  |  |
| --- | --- |
|  | Entering a Modbus slave variable using the default DB name:   1. Set the cursor in the parameter field and type an m character. 2. Select "MB\_SLAVE\_DB" from the drop-list. 3. Set the cursor at the right side of the DB name (after the quote character) and enter a period character. 4. Select "MB\_SLAVE\_DB.HR\_Start\_Offset" from the drop list. |
|  |
|  |

## Extended\_Addressing

The Extended\_Addressing variable is accessed in a similar way as the HR\_Start\_Offset reference discussed above except that the Extended\_Addressing variable is a Boolean value. The Boolean value must be written by an output coil and not a move box.

Modbus slave addressing can be configured to be either a single byte (which is the Modbus standard) or double byte. Extended addressing is used to address more than 247 devices within a single network. Selecting extended addressing allows you to address a maximum of 64000 addresses. A Modbus function 1 frame is shown below as an example.

Table 8. Single-byte slave address (byte 0)

| **Function 1** | **Byte 0** | **Byte 1** | **Byte 2** | **Byte 3** | **Byte 4** | **Byte 5** |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Request | Slave addr. | F code | Start address | | Length of coils | |  |
| Valid Response | Slave addr. | F code | Length | Coil data | | |  |
| Error response | Slave addr. | 0x81 | E code |  |  |  |  |

Table 9. Double-byte slave address (byte 0 and byte 1)

|  | **Byte 0** | **Byte 1** | **Byte 2** | **Byte 3** | **Byte 4** | **Byte 5** | **Byte 6** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Request | Slave address | | F code | Start address | | Length of coils | |
| Valid Response | Slave address | | F code | Length | Coil data | | |
| Error response | Slave address | | 0x81 | E code |  |  |  |

## Condition codes

Table 10. MB\_SLAVE execution condition codes (communication and configuration errors) 1

| **STATUS (W#16#)** | **Description** |
| --- | --- |
| 80D1 | The receiver issued a flow control request to suspend an active transmission and never re-enabled the transmission during the specified wait time.  This error is also generated during hardware flow control when the receiver does not assert CTS within the specified wait time. |
| 80D2 | The transmit request was aborted because no DSR signal is received from the DCE. |
| 80E0 | The message was terminated because the receive buffer is full. |
| 80E1 | The message was terminated as a result of a parity error. |
| 80E2 | The message was terminated as a result of a framing error. |
| 80E3 | The message was terminated as a result of an overrun error. |
| 80E4 | The message was terminated as a result of the specified length exceeding the total buffer size. |
| 8180 | Invalid port ID value or error with MB\_COMM\_LOAD instruction |
| 8186 | Invalid Modbus station address |
| 8187 | Invalid pointer to MB\_HOLD\_REG DB: Area is too small |
| 818C | Invalid MB\_HOLD\_REG pointer to M memory or DB (DB area must allow both symbolic and direct address) |

Table 11. MB\_SLAVE execution condition codes (Modbus protocol errors) 1

| **STATUS (W#16#)** | **Response code from slave** | **Modbus protocol errors** |
| --- | --- | --- |
| 8380 | No response | CRC error |
| 8381 | 01 | Function code not supported or not supported within broadcasts |
| 8382 | 03 | Data length error |
| 8383 | 02 | Data address error or address outside the valid range of the DATA\_PTR area |
| 8384 | 03 | Data value error |
| 8385 | 03 | Data diagnostic code value not supported (function code 08) |

1 In addition to the MB\_SLAVE errors listed above, errors can be returned from the underlying PtP communication instructions.

---

### Legacy Modbus RTU examples


---

#### Example: Legacy Modbus RTU master program

MB\_COMM\_LOAD is initialized during start-up by using the first scan flag. Execution of MB\_COMM\_LOAD in this manner should only be done when the serial port configuration will not change at runtime.

**Network 1**: Configure/initialize the RS485 module communications port only once during the first scan.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/P3afZCG2bB0TLD9cO~junA-VBkTPlmjVZAl17lebjV9hA/content?v=6d6372cf807117ac)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/P3afZCG2bB0TLD9cO~junA-VBkTPlmjVZAl17lebjV9hA)

One MB\_MASTER instruction is used in the program cycle OB to communicate with a single slave. Additional MB\_MASTER instructions can be used in the program cycle OB to communicate with other slaves, or one MB\_MASTER FB could be re-used to communicate with additional slaves.

**Network 2**: Read 100 words of holding register data from location 400001 on slave #2 to memory location MW500-MW698.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/PicMVptPnyjrmfOLK85fXA-VBkTPlmjVZAl17lebjV9hA/content?v=d82e264c133dc0ac)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/PicMVptPnyjrmfOLK85fXA-VBkTPlmjVZAl17lebjV9hA)

**Network 3**: Move the first 3 words of the holding register data that has been read to some other location, and set a DONE history bit. This network also sets an ERROR history bit and saves the STATUS word to another location in the event of an error.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/~7d~ENePkdtQER~MISlGXg-VBkTPlmjVZAl17lebjV9hA/content?v=494dfded1b97830e)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/~7d~ENePkdtQER~MISlGXg-VBkTPlmjVZAl17lebjV9hA)

**Network 4**: Write 64 bits of data from MW600-MW607 to output bit locations 00017 to 00081 on slave #2.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/ZwTZz6j7KYEoDnqX1Q_a3w-VBkTPlmjVZAl17lebjV9hA/content?v=7b9433000315c430)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/ZwTZz6j7KYEoDnqX1Q_a3w-VBkTPlmjVZAl17lebjV9hA)

**Network 5**: Set a DONE history bit when the write is complete. If an error occurs, the program sets an ERROR history bit and saves the STATUS code.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/y5aE2fUWRmSUPwyRbe5bpg-VBkTPlmjVZAl17lebjV9hA/content?v=504cabe2db614210)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/y5aE2fUWRmSUPwyRbe5bpg-VBkTPlmjVZAl17lebjV9hA)

---

#### Example: Legacy Modbus RTU slave program

MB\_COMM\_LOAD shown below is initialized each time "Tag\_1" is enabled.

Execution of MB\_COMM\_LOAD in this manner should only be done when the serial port configuration will change at runtime, as a result of HMI configuration.

**Network 1**: Initialize the RS485 module parameters each time they are changed by an HMI device.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/5nwOfhU_P2dhCianXMU8qw-VBkTPlmjVZAl17lebjV9hA/content?v=376795db2ef9787b)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/5nwOfhU_P2dhCianXMU8qw-VBkTPlmjVZAl17lebjV9hA)

MB\_SLAVE shown below is placed in a cyclic OB that is executed every 10ms. While this does not give the absolute fastest response by the slave, it does provide good performance at 9600 baud for short messages (20 bytes or less in the request).

**Network 2**: Check for Modbus master requests during each scan. The Modbus holding register is configured for 100 words starting at MW1000.

[![](https://docs.tia.siemens.cloud/api/khub/maps/VBkTPlmjVZAl17lebjV9hA/resources/kW_9np9F2wcRPqHXQVshrw-VBkTPlmjVZAl17lebjV9hA/content?v=93a4a30509346ea9)](https://docs.tia.siemens.cloud/viewer/attachment/VBkTPlmjVZAl17lebjV9hA/kW_9np9F2wcRPqHXQVshrw-VBkTPlmjVZAl17lebjV9hA)

---

## Industrial Remote Communication (IRC)


---

### Telecontrol CPs overview

Industrial Remote Communication provides access to widely distributed machines, plants, and applications of different sizes securely and economically. Industrial Remote Communications includes the following means of communication through CP modules:

- TeleControl: Telecontrol is the connection of process stations (Remote Terminal Units/RTUs) that are distributed over a wide geographical area to one or more central process control systems for the purpose of monitoring and control. Various different transmission components in the Remote Networks product spectrum support remote communication over a range of public and private networks. Special telecontrol protocols perform event-driven or cyclic exchange of process data, which permits efficient control of the overall process.
- TeleService: Teleservice involves data exchange with distant technical systems (machines, plants, computers, etc.) for the purpose of error detection, diagnostics, maintenance, repair, or optimization.
- Additional applications for remote communication, for example surveillance, smart grid applications, and condition monitoring.

## TeleControl CPs for the S7-1200

For TeleControl applications, the following communications processors, many of which also provide access to the S7‑1200 [Web server](https://docs.tia.siemens.cloud/r/VBkTPlmjVZAl17lebjV9hA/H8v_ZyWzJV4IpD~luNGAwg?section=X05a9645e263fbf69039c35b0ff635f64), are available:

- **CP 1243‑1****:**

  - Article number: 6GK7 243‑1BX30‑0XE0
  - Communications processor for connecting the SIMATIC S7-1200 to Industrial Ethernet or via the Internet to the following control center systems:

    - Telecontrol server (OPC server application TCSB V3)

    - DNP3 master station

    - IEC 60870-5 master station
  - With the help of VPN technology and the firewall, the CP allows protected access to the S7-1200.
  - You can use the CP as an interface extension of the CPU. In this role, it serves the purpose of network separation.
  - You communicate between the CP and CPU using configurable data points that access PLC tags.
- **CP 1243‑7 LTE-xx****:**

  - Communications processor for connecting the SIMATIC S7-1200 via a mobile network to the following control center systems:

    - Telecontrol server (OPC server application TCSB V3)

    - DNP3 master station

    - IEC 60870-5 master station
  - Communications processor for connecting the SIMATIC S7-1200 via mobile network to the following control center systems:
  - Support of the following mobile wireless specifications: GSM, UMTS (3G), LTE (4G)
  - To cover countries with different mobile wireless specifications, the CP is available in two variants:

    - CP 1243‑7 LTE‑US:

    - North American standard

    - Article number: 6GK7 243‑7SX30‑0XE0

    - CP 1243‑7 LTE‑EU:

    - Western European standard

    - Article number: 6GK7 243‑7KX30‑0XE0
  - With the help of VPN technology and the firewall, the CP allows protected access to the S7-1200.
  - You can use the CP as an additional Ethernet interface of the CPU for S7 communication.
  - You communicate between the CP and CPU using configurable data points that access PLC tags.
- **CP 1243‑8 IRC****:**

  - Article number: 6GK7 242‑8RX30‑0XE0
  - Communications processor for connecting the SIMATIC S7-1200 to an ST7 network, data point configuration, and VPN

Note:

You must have TeleControl Server Basic software for TeleControl applications for CPs other than the CP 1243‑1.

## Secure communication

The well-proven SINAUT ST7 protocol or the standardized DNP3 or IEC 60870‑5 protocol adds [security to Industrial Remote Communication](https://new.siemens.com/global/en/products/automation/industrial-communication/industrial-remote-communication.html). The TeleControl solution provides comprehensive measures to prevent data falsification and loss. Each transmission module has a large memory for several thousand data frames, which offers the ability to bridge downtimes in the transmission link. Dedicated VPN solutions protect special IP-based networks.

The CP 1243-1 communications processor securely connects the SIMATIC S7‑1200 controller to Ethernet networks. With its integrated firewall (Stateful Inspection) and VPN protocol (IPsec) security functions, the communications processor helps protect S7‑1200 stations and lower-level networks against unauthorized access and helps protect data transmission against manipulation and espionage by encryption. Furthermore, the CP can also be used for integrating the S7-1200 station into the TeleControl Server Basic control center software using IP-based remote networks.

---

### Further information

The following CP manuals provide detailed information on connection, requirements, applications, block instructions, accessories, and configuration examples:

- [CP 1243-1 Operating Instructions](https://support.industry.siemens.com/cs/ww/en/view/103948898)
- [CP 1243-7 LTE Operating Instructions](https://support.industry.siemens.com/cs/ww/en/view/109476704)
- [CP 1243-8 IRC Operating Instructions](https://support.industry.siemens.com/cs/ww/en/view/109777054)

For other information and documentation on these S7-1200 SIMATIC telecontrol CP modules, please visit the following links:

- [CP 1243-1](https://support.industry.siemens.com/cs/ww/en/ps/15922)
- [CP 1243-7 LTE](https://support.industry.siemens.com/cs/ww/en/ps/15924)
- [CP 1243-8 IRC](https://support.industry.siemens.com/cs/ww/en/ps/21162)
- [Firmware updates as available](https://support.industry.siemens.com/cs/ww/en/ps/21770/dl)