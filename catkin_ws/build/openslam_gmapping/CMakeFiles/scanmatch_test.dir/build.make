# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
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
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/build

# Include any dependencies generated for this target.
include openslam_gmapping/CMakeFiles/scanmatch_test.dir/depend.make

# Include the progress variables for this target.
include openslam_gmapping/CMakeFiles/scanmatch_test.dir/progress.make

# Include the compile flags for this target's objects.
include openslam_gmapping/CMakeFiles/scanmatch_test.dir/flags.make

openslam_gmapping/CMakeFiles/scanmatch_test.dir/scanmatcher/scanmatch_test.cpp.o: openslam_gmapping/CMakeFiles/scanmatch_test.dir/flags.make
openslam_gmapping/CMakeFiles/scanmatch_test.dir/scanmatcher/scanmatch_test.cpp.o: /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/src/openslam_gmapping/scanmatcher/scanmatch_test.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object openslam_gmapping/CMakeFiles/scanmatch_test.dir/scanmatcher/scanmatch_test.cpp.o"
	cd /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/build/openslam_gmapping && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/scanmatch_test.dir/scanmatcher/scanmatch_test.cpp.o -c /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/src/openslam_gmapping/scanmatcher/scanmatch_test.cpp

openslam_gmapping/CMakeFiles/scanmatch_test.dir/scanmatcher/scanmatch_test.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/scanmatch_test.dir/scanmatcher/scanmatch_test.cpp.i"
	cd /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/build/openslam_gmapping && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/src/openslam_gmapping/scanmatcher/scanmatch_test.cpp > CMakeFiles/scanmatch_test.dir/scanmatcher/scanmatch_test.cpp.i

openslam_gmapping/CMakeFiles/scanmatch_test.dir/scanmatcher/scanmatch_test.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/scanmatch_test.dir/scanmatcher/scanmatch_test.cpp.s"
	cd /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/build/openslam_gmapping && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/src/openslam_gmapping/scanmatcher/scanmatch_test.cpp -o CMakeFiles/scanmatch_test.dir/scanmatcher/scanmatch_test.cpp.s

# Object files for target scanmatch_test
scanmatch_test_OBJECTS = \
"CMakeFiles/scanmatch_test.dir/scanmatcher/scanmatch_test.cpp.o"

# External object files for target scanmatch_test
scanmatch_test_EXTERNAL_OBJECTS =

/afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/devel/lib/openslam_gmapping/scanmatch_test: openslam_gmapping/CMakeFiles/scanmatch_test.dir/scanmatcher/scanmatch_test.cpp.o
/afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/devel/lib/openslam_gmapping/scanmatch_test: openslam_gmapping/CMakeFiles/scanmatch_test.dir/build.make
/afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/devel/lib/openslam_gmapping/scanmatch_test: /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/devel/lib/libscanmatcher.so
/afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/devel/lib/openslam_gmapping/scanmatch_test: /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/devel/lib/liblog.so
/afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/devel/lib/openslam_gmapping/scanmatch_test: /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/devel/lib/libsensor_range.so
/afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/devel/lib/openslam_gmapping/scanmatch_test: /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/devel/lib/libsensor_odometry.so
/afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/devel/lib/openslam_gmapping/scanmatch_test: /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/devel/lib/libsensor_base.so
/afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/devel/lib/openslam_gmapping/scanmatch_test: /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/devel/lib/libutils.so
/afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/devel/lib/openslam_gmapping/scanmatch_test: openslam_gmapping/CMakeFiles/scanmatch_test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/devel/lib/openslam_gmapping/scanmatch_test"
	cd /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/build/openslam_gmapping && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/scanmatch_test.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
openslam_gmapping/CMakeFiles/scanmatch_test.dir/build: /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/devel/lib/openslam_gmapping/scanmatch_test

.PHONY : openslam_gmapping/CMakeFiles/scanmatch_test.dir/build

openslam_gmapping/CMakeFiles/scanmatch_test.dir/clean:
	cd /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/build/openslam_gmapping && $(CMAKE_COMMAND) -P CMakeFiles/scanmatch_test.dir/cmake_clean.cmake
.PHONY : openslam_gmapping/CMakeFiles/scanmatch_test.dir/clean

openslam_gmapping/CMakeFiles/scanmatch_test.dir/depend:
	cd /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/src /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/src/openslam_gmapping /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/build /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/build/openslam_gmapping /afs/inf.ed.ac.uk/user/s19/s1911027/catkin_ws/build/openslam_gmapping/CMakeFiles/scanmatch_test.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : openslam_gmapping/CMakeFiles/scanmatch_test.dir/depend

