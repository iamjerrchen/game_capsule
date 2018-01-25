# Adventure Game Capsule

Feed the capsule a adventure game story and play! The foundations will be based on three adventure game characteristics: events, event situations, and options,

## Story Input Structure

Example Json Format:

The following are keywords and must remain unchanged: 'game_name', 'start_event', 'events', 'situation', and 'options'

```json
{
    "game_name" : "OSRS",
    "start_event" : "Lumbridge",
    "events": {
        "Lumbridge" : {
            "situation" : "You're a noob starting in Lumbridge the castle of the duke.\n Where do you want to travel first?",
            "options" : {
                "Varrock" : "Walk to Varrock.",
                "Faldor" : "Walk to Faldor.",
                "Beg" : "Beg veteran players for money."
            }
        },
        "Varrock" : {
            "situation" : "You arrived in Varrock, but the guards mistaken you for a thief, so they imprisoned you.",
            "options" : {}
        },
        "Faldor" : {
            "situation" : "You arrived in Faldor. You attempt to find something to do.",
            "options" : {
                "Lumbridge" : "Faldor is boring, let's go back to Lumbridge",
                "Beg" : "Beg veteran players for money."
            }
        },
        "Beg" : {
            "situation" : "You attempt to flirt with some of the veteran players, but failed.\n A couple of the players reported you for solicitation.",
            "options" : {}
        },
    }
}
```

Under the 'events' dictionary, you can add as many events as you want. Simply copy and paste the format and fill in the details. Add more 'options' as necessary. Events where options is empty will automatically be an end event.

```json
"name of event" : {
    "situation" : "Fill Me",
    "options" : {
        "event name1" : "Fill Me",
        "event name2" : "Fill Me",
        "event name3" : "Fill Me"
    }
},
```

