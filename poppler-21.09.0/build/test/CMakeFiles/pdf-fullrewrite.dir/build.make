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
include test/CMakeFiles/pdf-fullrewrite.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include test/CMakeFiles/pdf-fullrewrite.dir/compiler_depend.make

# Include the progress variables for this target.
include test/CMakeFiles/pdf-fullrewrite.dir/progress.make

# Include the compile flags for this target's objects.
include test/CMakeFiles/pdf-fullrewrite.dir/flags.make

test/CMakeFiles/pdf-fullrewrite.dir/pdf-fullrewrite.cc.o: test/CMakeFiles/pdf-fullrewrite.dir/flags.make
test/CMakeFiles/pdf-fullrewrite.dir/pdf-fullrewrite.cc.o: ../test/pdf-fullrewrite.cc
test/CMakeFiles/pdf-fullrewrite.dir/pdf-fullrewrite.cc.o: test/CMakeFiles/pdf-fullrewrite.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/iris_linux/Experiment-Design/poppler-21.09.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object test/CMakeFiles/pdf-fullrewrite.dir/pdf-fullrewrite.cc.o"
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build/test && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT test/CMakeFiles/pdf-fullrewrite.dir/pdf-fullrewrite.cc.o -MF CMakeFiles/pdf-fullrewrite.dir/pdf-fullrewrite.cc.o.d -o CMakeFiles/pdf-fullrewrite.dir/pdf-fullrewrite.cc.o -c /home/iris_linux/Experiment-Design/poppler-21.09.0/test/pdf-fullrewrite.cc

test/CMakeFiles/pdf-fullrewrite.dir/pdf-fullrewrite.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pdf-fullrewrite.dir/pdf-fullrewrite.cc.i"
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build/test && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/iris_linux/Experiment-Design/poppler-21.09.0/test/pdf-fullrewrite.cc > CMakeFiles/pdf-fullrewrite.dir/pdf-fullrewrite.cc.i

test/CMakeFiles/pdf-fullrewrite.dir/pdf-fullrewrite.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pdf-fullrewrite.dir/pdf-fullrewrite.cc.s"
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build/test && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/iris_linux/Experiment-Design/poppler-21.09.0/test/pdf-fullrewrite.cc -o CMakeFiles/pdf-fullrewrite.dir/pdf-fullrewrite.cc.s

test/CMakeFiles/pdf-fullrewrite.dir/__/utils/parseargs.cc.o: test/CMakeFiles/pdf-fullrewrite.dir/flags.make
test/CMakeFiles/pdf-fullrewrite.dir/__/utils/parseargs.cc.o: ../utils/parseargs.cc
test/CMakeFiles/pdf-fullrewrite.dir/__/utils/parseargs.cc.o: test/CMakeFiles/pdf-fullrewrite.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/iris_linux/Experiment-Design/poppler-21.09.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object test/CMakeFiles/pdf-fullrewrite.dir/__/utils/parseargs.cc.o"
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build/test && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT test/CMakeFiles/pdf-fullrewrite.dir/__/utils/parseargs.cc.o -MF CMakeFiles/pdf-fullrewrite.dir/__/utils/parseargs.cc.o.d -o CMakeFiles/pdf-fullrewrite.dir/__/utils/parseargs.cc.o -c /home/iris_linux/Experiment-Design/poppler-21.09.0/utils/parseargs.cc

test/CMakeFiles/pdf-fullrewrite.dir/__/utils/parseargs.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pdf-fullrewrite.dir/__/utils/parseargs.cc.i"
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build/test && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/iris_linux/Experiment-Design/poppler-21.09.0/utils/parseargs.cc > CMakeFiles/pdf-fullrewrite.dir/__/utils/parseargs.cc.i

test/CMakeFiles/pdf-fullrewrite.dir/__/utils/parseargs.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pdf-fullrewrite.dir/__/utils/parseargs.cc.s"
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build/test && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/iris_linux/Experiment-Design/poppler-21.09.0/utils/parseargs.cc -o CMakeFiles/pdf-fullrewrite.dir/__/utils/parseargs.cc.s

# Object files for target pdf-fullrewrite
pdf__fullrewrite_OBJECTS = \
"CMakeFiles/pdf-fullrewrite.dir/pdf-fullrewrite.cc.o" \
"CMakeFiles/pdf-fullrewrite.dir/__/utils/parseargs.cc.o"

# External object files for target pdf-fullrewrite
pdf__fullrewrite_EXTERNAL_OBJECTS =

test/pdf-fullrewrite: test/CMakeFiles/pdf-fullrewrite.dir/pdf-fullrewrite.cc.o
test/pdf-fullrewrite: test/CMakeFiles/pdf-fullrewrite.dir/__/utils/parseargs.cc.o
test/pdf-fullrewrite: test/CMakeFiles/pdf-fullrewrite.dir/build.make
test/pdf-fullrewrite: test/CMakeFiles/pdf-fullrewrite.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/iris_linux/Experiment-Design/poppler-21.09.0/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable pdf-fullrewrite"
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build/test && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/pdf-fullrewrite.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
test/CMakeFiles/pdf-fullrewrite.dir/build: test/pdf-fullrewrite
.PHONY : test/CMakeFiles/pdf-fullrewrite.dir/build

test/CMakeFiles/pdf-fullrewrite.dir/clean:
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build/test && $(CMAKE_COMMAND) -P CMakeFiles/pdf-fullrewrite.dir/cmake_clean.cmake
.PHONY : test/CMakeFiles/pdf-fullrewrite.dir/clean

test/CMakeFiles/pdf-fullrewrite.dir/depend:
	cd /home/iris_linux/Experiment-Design/poppler-21.09.0/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/iris_linux/Experiment-Design/poppler-21.09.0 /home/iris_linux/Experiment-Design/poppler-21.09.0/test /home/iris_linux/Experiment-Design/poppler-21.09.0/build /home/iris_linux/Experiment-Design/poppler-21.09.0/build/test /home/iris_linux/Experiment-Design/poppler-21.09.0/build/test/CMakeFiles/pdf-fullrewrite.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : test/CMakeFiles/pdf-fullrewrite.dir/depend

