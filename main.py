import colorsys
import random

def rgb_to_hex(rgb_color):
    """Converts an RGB tuple (0-255) to a hexadecimal color string."""
    return '#%02x%02x%02x' % rgb_color

def generate_palette(mood):
    """
    Simulates an AI design tool generating a color palette based on a mood.
    This is a simplified rule-based system, not actual AI, demonstrating
    the concept of AI assistance in creative tasks.
    """
    # Define parameters for different moods. This is where an AI would learn patterns.
    mood_map = {
        "calm": {"hue_range": (0.55, 0.7), "saturation": 0.4, "lightness": 0.6}, # Blues/Greens
        "vibrant": {"hue_range": (0.0, 1.0), "saturation": 0.9, "lightness": 0.7}, # Bright, varied
        "professional": {"hue_range": (0.6, 0.8), "saturation": 0.3, "lightness": 0.5}, # Cool, muted
        "energetic": {"hue_range": (0.05, 0.15), "saturation": 0.8, "lightness": 0.7}, # Reds/Oranges
        "playful": {"hue_range": (0.2, 0.4), "saturation": 0.7, "lightness": 0.8}, # Yellows/Greens
    }

    # Default if mood not found, simulating an AI's fallback or 'best guess'.
    if mood.lower() not in mood_map:
        print(f"Mood '{mood}' not recognized. Using a default 'vibrant' palette.")
        mood_params = mood_map["vibrant"]
    else:
        mood_params = mood_map[mood.lower()]

    # Pick a base hue within the defined range for the mood.
    base_h = random.uniform(*mood_params["hue_range"]) if "hue_range" in mood_params else random.random()
    base_s = mood_params.get("saturation", 0.7)
    base_l = mood_params.get("lightness", 0.6)

    palette_hsl = []
    # Generate colors based on color theory (analogous, complementary, etc.)
    # This mimics how an AI might apply design principles.
    palette_hsl.append((base_h, base_s, base_l)) # Base color
    palette_hsl.append(((base_h + 0.08) % 1.0, base_s, base_l)) # Analogous 1
    palette_hsl.append(((base_h - 0.08) % 1.0, base_s, base_l)) # Analogous 2
    palette_hsl.append(((base_h + 0.5) % 1.0, base_s * 0.7, base_l * 0.8)) # Complementary (slightly desaturated/darker)
    palette_hsl.append((base_h, base_s * 0.2, (base_l + 0.2) % 1.0)) # Desaturated accent/neutral

    hex_palette = []
    for h, s, l in palette_hsl:
        # Convert HSL to RGB, then to hex for output.
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        hex_palette.append(rgb_to_hex((int(r * 255), int(g * 255), int(b * 255))))

    return hex_palette

if __name__ == "__main__":
    print("Welcome to the AI-powered Color Palette Generator Simulation!")
    print("Enter a mood (e.g., calm, vibrant, professional, energetic, playful) or 'exit' to quit.")

    while True:
        user_input = input("\nEnter a mood: ").strip()
        if user_input.lower() == 'exit':
            break

        # Simulate AI processing the user's request.
        print(f"\nAI is generating a palette for '{user_input}'...")
        palette = generate_palette(user_input)

        print(f"Generated Palette for '{user_input}':")
        for i, color_hex in enumerate(palette):
            print(f"  Color {i+1}: {color_hex}")
        print("\n(Note: This is a simplified, rule-based simulation of AI assistance in design.)")
