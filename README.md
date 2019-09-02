![TEXGINE](https://i.imgur.com/3YzforU.gif)

A simple engine for creating text based games by writing stories using XML. 
## Basic mechanics
The player traverses rooms, gaining effects and items while using effects and items to interact with objects called **interactables**. 

## Writing a story
The basic layout of story is the following
```XML
<stories>
<story>
    <name>Coats and Red</name>
    <startRoom>bedroom</startRoom>
    <description>A story of love, loss, and fucking awesomeness.</description>

    <player>
        <name>Default Player</name>
        <description>This is an example of a default set-up</description>
        <effects>defaultEffect</effects>
        <items>Self defaultItems</items>
        <art>:)</art>
    </player>

    <room>
        <name>bedroom</name>
        <description>a bedroom</description>
        <art>bed</art>
        <interactables>Bed</interactables>
    </room>


    <interactable>
        <name>Bed</name>
        <description>A cold metal framed bed that squeeks without presence.</description>
        <requiredEffects></requiredEffects>
        <items></items>
        <action>
            <name>Cut up the bed</name>
            <description>You shred up the bed to pieces</description>
            <failDescription>Your knife isn't sharp enough</failDescription>

            <item>Knife</item>

            <requiredEffects>sharpKnife</requiredEffects>
            <givenEffects>bluntKnife</givenEffects>
            <removedEffects>sharpKnife</removedEffects>

            <requiredItems>Knife</requiredItems>
            <givenItems></givenItems>
            <removedItems></removedItems>

            <newDesc>The carcass of a shredded mattress.</newDesc>
            <newItems>Golden Key</newItems>
            <newArt>Golden Key</newArt>
            <newInteractables></newInteractables>
        </action>
    </interactable>


    <item>
        <name>Knife</name>
        <description>A steely blade that glimmers in the sun.</description>
        <sellable>False</sellable>
        <value>100</value>
    </item>

    <effect>
        <name>sharpKnife</name>
        <description>You're knife is now sharp.</description>
        <isRoomChange>False</isRoomChange>
    </effect>

</story>


</stories>
```
The root `stories` object contains multiple `story` objects. A `story` contains multiple `item`, `interactable`, and `effect` objects with their respective information. 

### Interactables & Actions
Interactables are objects within the text based game that are interactable by the player. They can combine themselves, or items with the interactable for a specific outcome. This is called an `action`. The `action` can change the `interactable`, manipulate `effects` and/or `items`. 
```XML
    <interactable>
        <name>Bed</name>
        <description>A cold metal framed bed that squeeks without presence.</description>
        <requiredEffects></requiredEffects>
        <items></items>
        <action>
            <name>Cut up the bed</name>
            <description>You shred up the bed to pieces</description>
            <failDescription>Your knife isn't sharp enough</failDescription>

            <item>Knife</item>

            <requiredEffects>sharpKnife</requiredEffects>
            <givenEffects>bluntKnife</givenEffects>
            <removedEffects>sharpKnife</removedEffects>

            <requiredItems>Knife</requiredItems>
            <givenItems></givenItems>
            <removedItems></removedItems>

            <newDesc>The carcass of a shredded mattress.</newDesc>
            <newItems>Golden Key</newItems>
            <newArt>Golden Key</newArt>
            <newInteractables></newInteractables>
        </action>
    </interactable>
```
This interactable has an action that required a knife and the effect `sharpKnife`. The player will combine the knife object with this interactable which will trigger this action. If the player doesn't have the required effect then the `failDescription` will show, else the action is executed. 

### Room Traversal
Room traversal is acheived via an effect given by an action:
```XML
    <effect>
        <name>hallwayChange</name>
        <description>You're now in the hallway.</description>
        <isRoomChange roomname="hallway">True</isRoomChange>
    </effect>
```
The controller will check an effect that is given to the player and if it is a `isRoomChange` effect then the `roomname` attribute will be extracted and the player will then be switched to that room. Multiple interactables in a room can give room change effects so stories do not have to be linear. 

### Player Character
```XML
    <player>
        <name>Default Player</name>
        <description>This is an example of a default set-up</description>
        <effects>defaultEffect</effects>
        <items>Self defaultItems</items>
        <art>:)</art>
    </player>
```
You can add an optional `player` object to the game XML to give the player a preset character or loadout. You can either set up a character that the player has to play with a preset name, description etc or you can keep those blank to allow the player to set their own name, description etc. Effects and Items will be loaded into the player's game irrespective of whether or not you've chosen to set up the name, description or art. Do not add the player object or keep it blank if you'd like for all player data to be set during the story. 



## Installation & Use
Requirements:
* Python 3.7
* untangle

Run `controller.py`. 
