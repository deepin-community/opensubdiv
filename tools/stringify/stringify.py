#
#   Copyright 2022 Pixar
#
#   Licensed under the Apache License, Version 2.0 (the "Apache License")
#   with the following modification; you may not use this file except in
#   compliance with the Apache License and the following modification to it:
#   Section 6. Trademarks. is deleted and replaced with:
#
#   6. Trademarks. This License does not grant permission to use the trade
#      names, trademarks, service marks, or product names of the Licensor
#      and its affiliates, except as required to comply with Section 4(c) of
#      the License and to reproduce the content of the NOTICE file.
#
#   You may obtain a copy of the Apache License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the Apache License with the above modification is
#   distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#   KIND, either express or implied. See the Apache License for the specific
#   language governing permissions and limitations under the Apache License.
#

from __future__ import print_function
import sys

def stringify(s):
    withinStringConstant = False

    result = ""
    for i in range(len(s)-1):
        # escape double quotes
        if s[i] == '"':
            result += '\\'
            withinStringConstant = not withinStringConstant

        if s[i] == '\\' and i == len(s)-2:
            return '"' + result + '"\n'

        # escape backslash
        if withinStringConstant and s[i] == '\\':
            result += '\\'

        result += s[i]

    return '"' + result + '\\n"\n'

def stringifyFile(inputFilename, outputFilename):
    with open(inputFilename, "r") as inputFile, \
         open(outputFilename, "w") as outputFile:
        for line in inputFile:
            outputFile.write(stringify(line))
        outputFile.write('"\\n"\n')

if len(sys.argv) != 3:
    print("Usage: stringify input-file output-file")
    sys.exit(1)

stringifyFile(sys.argv[1], sys.argv[2])

