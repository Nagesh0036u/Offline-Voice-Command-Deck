import streamlit as st
from automation import execute_command
from command_manager import get_all_commands, add_command
from transcript import log_command, get_history, clear_history
from voice_listener import listen

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="Offline Voice Command Deck",
    page_icon="🎤",
    layout="wide"
)

# -----------------------------------
# TITLE
# -----------------------------------
st.title("🎤 Offline Voice Command Deck")

st.markdown("""
### 🚀 Personal Offline AI Assistant

✔ Execute Windows Commands

✔ Voice Control (Offline)

✔ Custom Commands

✔ Transcript History

✔ Works Without Internet (After Model Download)
""")

st.divider()

# ===================================
# TEXT COMMAND
# ===================================

st.subheader("⌨️ Execute Text Command")

command = st.text_input(
    "Enter Command",
    placeholder="Example: open calculator"
)

col1, col2 = st.columns(2)

with col1:

    if st.button("🚀 Execute Command", use_container_width=True):

        if command.strip():

            success = execute_command(command)

            if success:
                log_command(command)
                st.success(f"✅ Executed : {command}")
            else:
                st.error("❌ Unknown command.")

        else:
            st.warning("Please enter a command.")

# ===================================
# VOICE COMMAND
# ===================================

with col2:

    if st.button("🎤 Start Listening", use_container_width=True):

        status = st.empty()

        status.info("🎤 Listening... Please Speak")

        voice_command = listen()

        status.empty()

        if voice_command:

            st.success(f"🗣 You said: {voice_command}")

            success = execute_command(voice_command)

            if success:
                log_command(voice_command)
                st.success("✅ Command Executed")

            else:
                st.error("Unknown Command")

        else:

            st.error("No Voice Detected")

st.divider()

# ===================================
# AVAILABLE COMMANDS
# ===================================

st.subheader("📋 Available Commands")

commands = get_all_commands()

for cmd, action in commands.items():

    st.info(f"**{cmd}** ➜ {action}")

st.divider()

# ===================================
# ADD NEW COMMAND
# ===================================

st.subheader("➕ Add New Command")

new_command = st.text_input(
    "Command Name",
    placeholder="Example: open spotify"
)

new_action = st.text_input(
    "Action",
    placeholder="Example: spotify.exe"
)

if st.button("💾 Save Command"):

    if new_command and new_action:

        add_command(new_command, new_action)

        st.success("✅ Command Saved Successfully")

        st.rerun()

    else:

        st.warning("Please fill both fields.")

st.divider()

# ===================================
# HISTORY
# ===================================

st.subheader("📜 Transcript")

history = get_history()

if history:

    for item in reversed(history):

        st.code(item.strip())

else:

    st.info("No commands executed yet.")

if st.button("🗑 Clear Transcript"):

    clear_history()

    st.success("Transcript Cleared")

    st.rerun()

st.divider()

st.caption("Developed using ❤️ Python + Streamlit + Faster Whisper")