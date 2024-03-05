
# Required

Ensure you have Python 3 installed.

# Example

Remove the "_Built with Mkdocs_" footer/ mkdocs credit from all the .html files in your site.

Drop the Python script into a folder beside the *site* folder that contains your HTML site after generation by Mkdocs.

Then run the script with this command:

```
python strip_built_with_banner.py
```

All "built with Mkdocs" lines will be removed.


# Note

Please add the Mkdocs credits in your site somewhere else convenient.
