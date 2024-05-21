
KV = """
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts
#:import MDTab widgets.MDTab

MDScreen:
    
    MDNavigationLayout:
        MDScreenManager:
            
            MDScreen:                    
    
                MDBoxLayout:
                    orientation: "vertical"
            
                    MDTopAppBar:
                        title: "Сколько должен"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        md_bg_color: app.md_bg_color
                        anchor_title: "left"
                    
                    MDTabs:
                        id: tabs
                        background_color: app.md_bg_color
                        tab_hint_x: True
                        allow_stretch: True

                        
                        MDTab:
                            title: f"[size=18sp][font={fonts[-1]['fn_regular']}]{md_icons['account-group']}[/size][/font] [size=18sp][/font][/ref] Участники"
                            MDBoxLayout:
                                padding: [20, 20, 20, 20]
                                MDFillRoundFlatButton:
                                    text: "Button"

                        MDTab:
                            title: f"[size=18sp][font={fonts[-1]['fn_regular']}]{md_icons['account-cash']}[/size][/font] [size=18sp][/font][/ref] Расчет"

                        
                    # MDLabel:
                    #     text: "Content"
                    #     halign: "center"

        
        MDNavigationDrawer:
            id: nav_drawer
"""
