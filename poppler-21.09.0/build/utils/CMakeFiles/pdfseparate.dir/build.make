# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/iris_linux/Experiment-Design/poppler-21.09.0

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/iris_linux/Experiment-Design/poppler-21.09.0/build

# Include any dependencies generated for this target.
include utils/CMakeFiles/pdfseparate.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include utils/CMakeFiles/pdfseparate.dir/compiler_depend.make

# Include the progress variables for this target.
include utils/CMakeFiles/pdfseparate.dir/progress.make

# Include the compile flags for this target's objects.
include utils/CMakeFiles/pdfseparate.dir/flags.make

utils/CMakeFiles/pdfseparate.dir/parseargs.cc.o: utils/CMakeFiles/pdfseparate.dir/flags.make
utils/CMakeFiles/pdfseparate.dir/parseargs.cc.o: ../utils/parseargs.cc
utils/CMakeFiles/pdfseparate.dir/parseargs.cc.o: utils/CMakeFiles/pdfseparate.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/iris_linux/Experiment-Design/poppler-21.09.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object utils/CMakeFiles/pdfseparate.dir/parseargs.cc.o"
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build/utils && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT utils/CMakeFiles/pdfseparate.dir/parseargs.cc.o -MF CMakeFiles/pdfseparate.dir/parseargs.cc.o.d -o CMakeFiles/pdfseparate.dir/parseargs.cc.o -c /home/iris_linux/Experiment-Design/poppler-21.09.0/utils/parseargs.cc

utils/CMakeFiles/pdfseparate.dir/parseargs.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pdfseparate.dir/parseargs.cc.i"
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build/utils && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/iris_linux/Experiment-Design/poppler-21.09.0/utils/parseargs.cc > CMakeFiles/pdfseparate.dir/parseargs.cc.i

utils/CMakeFiles/pdfseparate.dir/parseargs.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pdfseparate.dir/parseargs.cc.s"
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build/utils && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/iris_linux/Experiment-Design/poppler-21.09.0/utils/parseargs.cc -o CMakeFiles/pdfseparate.dir/parseargs.cc.s

utils/CMakeFiles/pdfseparate.dir/Win32Console.cc.o: utils/CMakeFiles/pdfseparate.dir/flags.make
utils/CMakeFiles/pdfseparate.dir/Win32Console.cc.o: ../utils/Win32Console.cc
utils/CMakeFiles/pdfseparate.dir/Win32Console.cc.o: utils/CMakeFiles/pdfseparate.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/iris_linux/Experiment-Design/poppler-21.09.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object utils/CMakeFiles/pdfseparate.dir/Win32Console.cc.o"
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build/utils && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT utils/CMakeFiles/pdfseparate.dir/Win32Console.cc.o -MF CMakeFiles/pdfseparate.dir/Win32Console.cc.o.d -o CMakeFiles/pdfseparate.dir/Win32Console.cc.o -c /home/iris_linux/Experiment-Design/poppler-21.09.0/utils/Win32Console.cc

utils/CMakeFiles/pdfseparate.dir/Win32Console.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pdfseparate.dir/Win32Console.cc.i"
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build/utils && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/iris_linux/Experiment-Design/poppler-21.09.0/utils/Win32Console.cc > CMakeFiles/pdfseparate.dir/Win32Console.cc.i

utils/CMakeFiles/pdfseparate.dir/Win32Console.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pdfseparate.dir/Win32Console.cc.s"
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build/utils && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/iris_linux/Experiment-Design/poppler-21.09.0/utils/Win32Console.cc -o CMakeFiles/pdfseparate.dir/Win32Console.cc.s

utils/CMakeFiles/pdfseparate.dir/pdfseparate.cc.o: utils/CMakeFiles/pdfseparate.dir/flags.make
utils/CMakeFiles/pdfseparate.dir/pdfseparate.cc.o: ../utils/pdfseparate.cc
utils/CMakeFiles/pdfseparate.dir/pdfseparate.cc.o: utils/CMakeFiles/pdfseparate.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/iris_linux/Experiment-Design/poppler-21.09.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object utils/CMakeFiles/pdfseparate.dir/pdfseparate.cc.o"
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build/utils && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT utils/CMakeFiles/pdfseparate.dir/pdfseparate.cc.o -MF CMakeFiles/pdfseparate.dir/pdfseparate.cc.o.d -o CMakeFiles/pdfseparate.dir/pdfseparate.cc.o -c /home/iris_linux/Experiment-Design/poppler-21.09.0/utils/pdfseparate.cc

utils/CMakeFiles/pdfseparate.dir/pdfseparate.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pdfseparate.dir/pdfseparate.cc.i"
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build/utils && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/iris_linux/Experiment-Design/poppler-21.09.0/utils/pdfseparate.cc > CMakeFiles/pdfseparate.dir/pdfseparate.cc.i

utils/CMakeFiles/pdfseparate.dir/pdfseparate.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pdfseparate.dir/pdfseparate.cc.s"
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build/utils && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/iris_linux/Experiment-Design/poppler-21.09.0/utils/pdfseparate.cc -o CMakeFiles/pdfseparate.dir/pdfseparate.cc.s

# Object files for target pdfseparate
pdfseparate_OBJECTS = \
"CMakeFiles/pdfseparate.dir/parseargs.cc.o" \
"CMakeFiles/pdfseparate.dir/Win32Console.cc.o" \
"CMakeFiles/pdfseparate.dir/pdfseparate.cc.o"

# External object files for target pdfseparate
pdfseparate_EXTERNAL_OBJECTS =

utils/pdfseparate: utils/CMakeFiles/pdfseparate.dir/parseargs.cc.o
utils/pdfseparate: utils/CMakeFiles/pdfseparate.dir/Win32Console.cc.o
utils/pdfseparate: utils/CMakeFiles/pdfseparate.dir/pdfseparate.cc.o
utils/pdfseparate: utils/CMakeFiles/pdfseparate.dir/build.make
utils/pdfseparate: utils/CMakeFiles/pdfseparate.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/iris_linux/Experiment-Design/poppler-21.09.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Linking CXX executable pdfseparate"
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build/utils && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/pdfseparate.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
utils/CMakeFiles/pdfseparate.dir/build: utils/pdfseparate
.PHONY : utils/CMakeFiles/pdfseparate.dir/build

utils/CMakeFiles/pdfseparate.dir/clean:
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build/utils && $(CMAKE_COMMAND) -P CMakeFiles/pdfseparate.dir/cmake_clean.cmake
.PHONY : utils/CMakeFiles/pdfseparate.dir/clean

utils/CMakeFiles/pdfseparate.dir/depend:
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/iris_linux/Experiment-Design/poppler-21.09.0 /home/iris_linux/Experiment-Design/poppler-21.09.0/utils /home/iris_linux/Experiment-Design/poppler-21.09.0/build /home/iris_linux/Experiment-Design/poppler-21.09.0/build/utils /home/iris_linux/Experiment-Design/poppler-21.09.0/build/utils/CMakeFiles/pdfseparate.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : utils/CMakeFiles/pdfseparate.dir/depend

