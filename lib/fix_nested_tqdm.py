# fix tqdm space: https://github.com/tqdm/tqdm/issues/433#issuecomment-511421546

from IPython.display import display, HTML

def fix_nested_tqdm ():
    display(HTML("""
        <style>
            .p-Widget.jp-OutputPrompt.jp-OutputArea-prompt:empty {
                  padding: 0;
                  border: 0;
            }
        </style>
    """))
