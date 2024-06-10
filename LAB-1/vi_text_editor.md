**Basic Navigation:**

* **`h`:** Move left one character.
* **`j`:** Move down one line.
* **`k`:** Move up one line.
* **`l`:** Move right one character.
* **`G`:** Go to the last line of the file.
* **`gg`:** Go to the first line of the file.
* **`n` (repeat):** Repeat the last movement command (e.g., `2j` moves down two lines).
* **`/pattern` (search):** Search for a pattern in the file and move the cursor to the first occurrence. Use `n` to find the next occurrence.

**Entering Text:**

* **`i`:** Insert text before the cursor (Insert mode).
* **`a`:** Append text after the cursor (Insert mode).
* **`O`:** Open a new line above the current line (Insert mode).
* **`o`:** Open a new line below the current line (Insert mode).
* **`Esc`:** Exit Insert mode and return to Command mode.

**Deleting Text:**

* **`x`:** Delete the character under the cursor.
* **`d` (delete with motion):** Delete text based on a motion command (e.g., `dd` deletes the current line, `dw` deletes the word under the cursor).
* **`X` (repeat delete):** Repeat the last deletion command (e.g., `3X` deletes three characters).

**Copying and Pasting:**

* **`y` (yank with motion):** Copy text based on a motion command (e.g., `yy` copies the current line, `yw` copies the word under the cursor).
* **`p`:** Paste the yanked text after the cursor.

**Saving and Exiting:**

* **`:w` (write):** Save the file without exiting vi.
* **`:q` (quit):** Exit vi without saving changes (use with caution!).
* **`:wq` (write and quit):** Save the file and exit vi.
* **`:q!` (quit forced):** Exit vi forcefully, even if there are unsaved changes.

**Additional Tips:**

* Use the `man vi` command for the full vi manual with detailed explanations.
* Consider using the `vim` editor, which is an extended version of vi with additional features and a more user-friendly interface.

By including these commands in your GitHub readme, you'll provide a valuable reference for those new to vi or needing a quick refresher.
