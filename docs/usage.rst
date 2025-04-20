Usage
=====

The CLI command to generate a json or csv from a dictionary file is:

Examples:

.. code-block:: bash

   dictionary-generator generate input.txt out/ --letters=a-c --format=json --case=lower
   dictionary-generator generate input.txt out/ --letters=a,c,f --merge --case=upper

Options:

- ``--letters``: Filter by first letter. Supports:
  - ``a`` → words starting with A (single letter option)
  - ``a-c`` → words starting with A, B, or C (inclusive option)
  - ``a,c,f`` → words starting with A, C, or F (exclusive option)
- ``--format``: Output format (``json`` or ``csv``)
- ``--case``: Word casing: ``lower``, ``upper``, or ``nochange``
- ``--merge``: Merge all output into one file
