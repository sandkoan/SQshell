from prompt_toolkit.styles import Style, style_from_pygments_cls, merge_styles 

def mystyle():
    style1 = Style.from_dict({
        'completion-menu.completion': 'bg:#008888 #ffffff',
        'completion-menu.completion.current': 'bg:#00aaaa #000000',
        'scrollbar.background': 'bg:#88aaaa',
        'scrollbar.button': 'bg:#222222',
        # 'bottom-toolbar': 'bg:#096f9e #0a8dc9',

        # Prompt
        'language': 'ansicyan bold',
        'arrow': '#9BD55C'
    })

    dialog_style = Style.from_dict({
        'dialog':             'bg:#88ff88',
        'dialog frame.label': 'bg:#ffffff #000000',
        'dialog.body':        'bg:#000000 #00ff00',
        'dialog shadow':      'bg:#00aa00',
    })

    style = merge_styles([
        style1,
        dialog_style
    ])

    return style
