# JetBrains High Contrast for Zed

A port of the JetBrains High Contrast accessibility theme for [Zed](https://zed.dev).

The theme combines dark editor backgrounds with bright syntax colors and subdued grey line numbers. In Rust, `self` and constants use purple italics, documentation comments use green italics, and regular comments use blue. The highlighting you see depends on the language's syntax captures.

## Installation

1. Open the command palette in Zed and run `zed: extensions`.
2. Search for **JetBrains High Contrast** and install it. The extension ID is `jb-high-contrast-theme`.
3. Run `theme selector: toggle` and select **JetBrains High Contrast**.

## Customization

Run `zed: open settings file` to edit your Zed settings. Add a `theme_overrides` entry for `JetBrains High Contrast` to customize individual colors or text styles. If you already have that entry, merge the properties into it.

For example, this makes regular comments use the same green as documentation comments while keeping their existing font style.

```json
{
  "theme_overrides": {
    "JetBrains High Contrast": {
      "syntax": {
        "comment": {
          "color": "#499936FF"
        }
      }
    }
  }
}
```

To make regular comments italic too, add `"font_style": "italic"` alongside `"color"`. Syntax overrides apply to every language using the matching capture in this theme.

### Rust documentation links

In Zed 1.27.0, Rustdoc references such as ``[`DecodeOptions::read_info`]`` share the surrounding documentation comment style. Changing the theme's link colors does not make these references stand out when idle. Persistent, separate styling needs support from Zed's Rust highlighting. The theme cannot tell whether a reference resolves.

Rust's documentation tool can report unresolved references through its built-in `rustdoc::broken_intra_doc_links` warning. See [the Rustdoc documentation](https://doc.rust-lang.org/rustdoc/lints.html#broken_intra_doc_links).

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

### Cursor and selection

For a white cursor and an opaque blue selection matching the corresponding JetBrains High Contrast colors, copy the full `players` array from the theme file into your `JetBrains High Contrast` override. Replace only its first entry with this object, keeping the remaining entries for collaborators.

```json
{
  "cursor": "#FFFFFFFF",
  "background": "#FFFFFFFF",
  "selection": "#006280FF"
}
```

### PHP built-in values and types

Zed's PHP highlighting uses `constant.builtin` for `true`, `false`, and `null`, and `type.builtin` for primitive types such as `int`. To make those captures orange, merge these entries into your override's `syntax` object.

```json
{
  "constant.builtin": {
    "color": "#ED864AFF",
    "font_style": "normal"
  },
  "type.builtin": {
    "color": "#ED864AFF",
    "font_weight": 400
  }
}
```

These capture names are shared with other languages, so this preference also affects matching captures outside PHP. Zed already falls back from `function.method` to `function` and from `variable.parameter` to `variable`; explicit entries are useful when you want a different style.

## Reviewing theme changes

Before publishing a theme change, install it as a development extension in Zed, select it, and open representative Rust and PHP files. Check syntax colors, comment styles, selection, search results, and wrap guides in the editor. Syntax styles belong inside each theme's `style.syntax` object.

For a release, update `extension.toml` and submit the version and source commit to the Zed extension registry. A source change reaches installed users through the published registry update. See [Zed's extension update guide](https://zed.dev/docs/extensions/publishing/updating-and-maintenance).

## Credits and license

Based on the High Contrast theme bundled with JetBrains IDEs. Distributed under the [MIT license](LICENSE).
