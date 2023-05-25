# Assembler for Custom ISA - Readme

## Introduction
Welcome to the custom ISA Assembler project! This Python-based tool assembler converts assembly instructions in the custom ISA syntax into corresponding machine code. It can handle various instructions, labels, and variables while ensuring proper syntax and error handling.

## Features
The assembler provides the following features:

1. **Instruction Handling**: The assembler supports a range of instructions defined by the custom ISA. It accurately parses and processes each instruction, considering the opcode, registers, memory addresses, and immediate values.

2. **Label Support**: Labels are crucial in code organization and control flow. The assembler recognizes labels marked by a trailing colon and handles them appropriately. Labels can be used as memory addresses in jump instructions.

3. **Variable Management**: The assembler supports the declaration of 16-bit variables at the beginning of the assembly program. Variables can be utilized as memory addresses in load and store instructions, enhancing code readability and flexibility.

4. **Error Detection and Reporting**: The assembler performs comprehensive error checking to ensure the integrity of the assembly code. It detects and reports various issues, such as typos in instruction or registers names, usage of undefined variables or labels, illegal use of the FLAGS register, improper immediate values, misuse of labels as variables or vice versa, variables not declared at the beginning, missing HLT instruction, and HLT not being used as the last instruction. Each error is accompanied by the corresponding line number for easy identification.

5. **Binary Code Generation**: If the assembly code is error-free, the assembler generates a corresponding binary file as output. Each line of the binary file represents a 16-bit binary number written using ASCII characters '0' and '1'. The resulting binary code accurately reflects the instructions and data defined in the assembly program.

## Usage
To utilize the custom ISA Assembler, follow these steps:

1. Prepare the assembly program: Write your assembly code in a text file, adhering to the syntax and guidelines specified in the project requirements. Each line should be one of the following types: empty, label, instruction, or variable definition.

2. Run the assembler: Execute the Python script that implements the assembler, providing the assembly program file as input as assembly.txt

3. Review the output: The assembler will generate one or more output files, depending on the result:
   - If there are no errors in the assembly program, a binary file containing the machine code will be produced. Each line of the binary file represents a 16-bit binary number.
   - If errors are encountered, an error notification file will be created, highlighting the first error located along with the corresponding line number. The error notification file assists in identifying and rectifying the issues in the assembly code.

4. Error handling: Review the error notification file to address the identified issues if errors are reported. Make the necessary corrections in the assembly program file and rerun the assembler until the code is error-free.

5. Utilize the binary code: Once the assembler successfully generates the binary file, you can use it as input for further processing or execution in an emulator or hardware system designed to interpret the custom ISA.

## Conclusion
The custom ISA Assembler is a powerful tool that simplifies converting assembly instructions into machine code. Its extensive support for instructions, labels, and variables, along with robust error detection and reporting capabilities, enables developers to create error-free and optimized assembly programs. You can seamlessly integrate your assembly programs into custom ISA-based systems by utilizing the generated binary code.

Please feel free to explore the provided Python implementation and make any necessary modifications or enhancements to suit your specific requirements. Happy assembling!
