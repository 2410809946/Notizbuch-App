from js import document
import asyncio

notes = []

def add_note():
    title = document.getElementById("note-title").value
    content = document.getElementById("note-content").value

    if title and content:
        note = {
            "title": title,
            "content": content
        }
        notes.append(note)
        render_notes()
        clear_form()

def delete_note(index):
    del notes[index]
    render_notes()

def render_notes():
    notes_container = document.getElementById("notes-container")
    notes_container.innerHTML = ""

    for index, note in enumerate(notes):
        note_element = document.createElement("div")
        note_element.className = "note"

        note_header = document.createElement("div")
        note_header.className = "note-header"
        note_header.innerHTML = f"<strong>{note['title']}</strong>"

        note_content = document.createElement("p")
        note_content.textContent = note["content"]

        note_actions = document.createElement("div")
        note_actions.className = "note-actions"
        delete_button = document.createElement("button")
        delete_button.textContent = "Löschen"
        delete_button.onclick = lambda e, idx=index: delete_note(idx)

        note_actions.appendChild(delete_button)

        note_element.appendChild(note_header)
        note_element.appendChild(note_content)
        note_element.appendChild(note_actions)

        notes_container.appendChild(note_element)

def clear_form():
    document.getElementById("note-title").value = ""
    document.getElementById("note-content").value = ""

async def main():
    while document.getElementById("note-form") is None:
        await asyncio.sleep(0.1)  # Kurze Verzögerung, um sicherzustellen, dass das DOM geladen ist
    note_form = document.getElementById("note-form")
    note_form.addEventListener("submit", lambda e: (e.preventDefault(), add_note()))

asyncio.ensure_future(main())