### OpenPDFLibrary

## 📋 Description

This library has the utility of reading files in PDF format

This library uses [tika-python](https://github.com/chrismattmann/tika-python) to read the files.

## 📃 Keywords

```robotframework
Get PDF Text        # Returns the PDF content in text format
Get PDF Text XHTML  # Returns the PDF content in XHTML format
Get PDF Metadata    # Returns the PDF header
```

### 🌟 Requirements

  - ``RobotFramework 3 or above.``
  - ``Java 8 or above.``

### 📜 Installation

  - install the package ``pip install openpdflibrary``
    - on the first run it can take a while or even open a java permission screen
   
## 🔥 Uses
  - Examples of Uses
    ```robotframework
    *** Settings ***
    Library  OpenPDFLibrary

    *** Test Cases ***
    reading pdf file
        ${raw_content}    Get PDF Text    file.pdf
        ${content_xhtml}    Get PDF Text XHTML    file.pdf
        ${meta}    Get PDF Metadata    file.pdf
        Log    Raw -> ${raw_content}
        Log    Xhtml -> ${content_xhtml}
        Log    Meta -> ${meta}
    ```
