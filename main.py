import os

EMOJI = '\U0001F916'  # Verified: 1 char, 4 bytes (U+1F916 ROBOT FACE 🤖)

out_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
out_path = os.path.join(out_dir, 'entry.txt')

os.makedirs(out_dir, exist_ok=True)
with open(out_path, 'w', encoding='utf-8', newline='') as f:
    f.write(EMOJI)

print(len(EMOJI.encode('utf-8')))
