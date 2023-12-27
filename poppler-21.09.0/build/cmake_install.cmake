# Install script for directory: /home/iris_linux/Experiment-Design/poppler-21.09.0

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/x86_64-linux-gnu/libpoppler.so.113.0.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/x86_64-linux-gnu/libpoppler.so.113"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/x86_64-linux-gnu" TYPE SHARED_LIBRARY FILES
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/build/libpoppler.so.113.0.0"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/build/libpoppler.so.113"
    )
  foreach(file
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/x86_64-linux-gnu/libpoppler.so.113.0.0"
      "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/x86_64-linux-gnu/libpoppler.so.113"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/x86_64-linux-gnu/libpoppler.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/x86_64-linux-gnu/libpoppler.so")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/x86_64-linux-gnu/libpoppler.so"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/x86_64-linux-gnu" TYPE SHARED_LIBRARY FILES "/home/iris_linux/Experiment-Design/poppler-21.09.0/build/libpoppler.so")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/x86_64-linux-gnu/libpoppler.so" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/x86_64-linux-gnu/libpoppler.so")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/x86_64-linux-gnu/libpoppler.so")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/poppler" TYPE FILE FILES
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Annot.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Array.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/CachedFile.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Catalog.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/CharCodeToUnicode.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/CMap.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/DateInfo.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Decrypt.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Dict.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Error.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/FileSpec.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/FontEncodingTables.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/FontInfo.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Form.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Function.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Gfx.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/GfxFont.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/GfxState.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/GfxState_helpers.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/GlobalParams.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Hints.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/JArithmeticDecoder.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/JBIG2Stream.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/JSInfo.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Lexer.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Link.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Linearization.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/LocalPDFDocBuilder.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/MarkedContentOutputDev.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Movie.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/NameToCharCode.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Object.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/OptionalContent.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Outline.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/OutputDev.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Page.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/PageTransition.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Parser.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/PDFDoc.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/PDFDocBuilder.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/PDFDocEncoding.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/PDFDocFactory.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/PopplerCache.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/ProfileData.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/PreScanOutputDev.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/PSTokenizer.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Rendition.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/CertificateInfo.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Stream-CCITT.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Stream.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/StructElement.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/StructTreeRoot.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/UnicodeMap.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/UnicodeMapFuncs.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/UnicodeMapTables.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/UnicodeTypeTable.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/UnicodeCClassTables.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/UnicodeCompTables.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/UnicodeDecompTables.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/ViewerPreferences.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/XRef.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/CharTypes.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/ErrorCodes.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/NameToUnicodeTable.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/PSOutputDev.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/TextOutputDev.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/SecurityHandler.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/StdinCachedFile.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/StdinPDFDocBuilder.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/BBoxOutputDev.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/UTF.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/Sound.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/build/poppler_private_export.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/build/poppler/poppler-config.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/SplashOutputDev.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/poppler/goo" TYPE FILE FILES
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/goo/GooTimer.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/goo/GooString.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/goo/gmem.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/goo/gdir.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/goo/gfile.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/goo/ImgWriter.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/goo/GooCheckedOps.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/goo/GooLikely.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/goo/gstrtod.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/goo/grandom.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/poppler/goo" TYPE FILE FILES "/home/iris_linux/Experiment-Design/poppler-21.09.0/goo/PNGWriter.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/poppler/goo" TYPE FILE FILES "/home/iris_linux/Experiment-Design/poppler-21.09.0/goo/JpegWriter.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/poppler/fofi" TYPE FILE FILES
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/fofi/FoFiBase.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/fofi/FoFiEncodings.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/fofi/FoFiTrueType.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/fofi/FoFiType1.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/fofi/FoFiType1C.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/fofi/FoFiIdentifier.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/poppler" TYPE FILE FILES "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/JPEG2000Stream.h")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/poppler/splash" TYPE FILE FILES
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/Splash.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/SplashBitmap.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/SplashClip.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/SplashErrorCodes.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/SplashFTFont.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/SplashFTFontEngine.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/SplashFTFontFile.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/SplashFont.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/SplashFontEngine.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/SplashFontFile.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/SplashFontFileID.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/SplashGlyphBitmap.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/SplashMath.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/SplashPath.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/SplashPattern.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/SplashScreen.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/SplashState.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/SplashTypes.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/SplashXPath.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/splash/SplashXPathScanner.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/poppler" TYPE FILE FILES
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/CairoFontEngine.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/CairoOutputDev.h"
    "/home/iris_linux/Experiment-Design/poppler-21.09.0/poppler/CairoRescaleBox.h"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/x86_64-linux-gnu/pkgconfig" TYPE FILE FILES "/home/iris_linux/Experiment-Design/poppler-21.09.0/build/poppler.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/x86_64-linux-gnu/pkgconfig" TYPE FILE FILES "/home/iris_linux/Experiment-Design/poppler-21.09.0/build/poppler-glib.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/x86_64-linux-gnu/pkgconfig" TYPE FILE FILES "/home/iris_linux/Experiment-Design/poppler-21.09.0/build/poppler-cpp.pc")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/iris_linux/Experiment-Design/poppler-21.09.0/build/utils/cmake_install.cmake")
  include("/home/iris_linux/Experiment-Design/poppler-21.09.0/build/glib/cmake_install.cmake")
  include("/home/iris_linux/Experiment-Design/poppler-21.09.0/build/test/cmake_install.cmake")
  include("/home/iris_linux/Experiment-Design/poppler-21.09.0/build/cpp/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/iris_linux/Experiment-Design/poppler-21.09.0/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
