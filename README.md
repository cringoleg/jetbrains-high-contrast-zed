# JetBrains High Contrast for Zed

A port of the JetBrains High Contrast accessibility theme for [Zed](https://zed.dev).

The theme combines dark editor backgrounds with bright syntax colors and subdued grey line numbers. It styles documentation comments in green italics and constants in purple italics. The highlighting you see depends on the language's syntax captures.

## Installation

1. Open the command palette in Zed and run `zed: extensions`.
2. Search for **JetBrains High Contrast** and install it. The extension ID is `jb-high-contrast-theme`.
3. Run `theme selector: toggle` and select **JetBrains High Contrast**.

## Customization

Run `zed: open settings file` to edit your Zed settings. Add a `theme_overrides` entry for `JetBrains High Contrast` to customize individual colors or text styles. If you already have that entry, merge the properties into it.

For example, this makes regular comments use the same green and italics as documentation comments.

```json
{
  "theme_overrides": {
    "JetBrains High Contrast": {
      "syntax": {
        "comment": {
          "color": "#499936FF",
          "font_style": "italic"
        }
      }
    }
  }
}
```

### Wrap guides

Wrap guides mark character columns with vertical lines. Enable them and specify their positions with `wrap_guides`. With `soft_wrap` set to `none`, setting `preferred_line_length` alone does not show a guide.

This example shows guides at columns 80, 100, and 120 and makes ordinary guides brighter than the theme default.

```json
{
  "show_wrap_guides": true,
  "wrap_guides": [80, 100, 120],
  "theme_overrides": {
    "JetBrains High Contrast": {
      "editor.wrap_guide": "#FFFFFF20",
      "editor.active_wrap_guide": "#FFFFFF1A"
    }
  }
}
```

`editor.wrap_guide` controls ordinary guides. `editor.active_wrap_guide` controls the guide Zed marks as active for the wrapping column. Its appearance depends on your wrapping settings. The last two digits in these eight-digit colors control opacity, from `00` (transparent) to `FF` (opaque).

See [Zed's theme override documentation](https://zed.dev/docs/themes#theme-overrides) and [wrap guide settings](https://zed.dev/docs/reference/all-settings#wrap-guides-vertical-rulers) for more options. The available theme properties are listed in [the theme file](themes/jb-high-contrast.json).

## Credits and license

Based on the High Contrast theme bundled with JetBrains IDEs. Distributed under the [MIT license](LICENSE).
