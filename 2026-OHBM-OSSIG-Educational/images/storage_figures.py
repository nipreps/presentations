# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "matplotlib>=3.10.9",
#     "pandas>=3.0.3",
#     "seaborn>=0.13.2",
# ]
# ///
import pandas as pd
import seaborn as sns
import seaborn.objects as so
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.patches import Patch

sns.set_theme(style="whitegrid")

# ── Tidy data ─────────────────────────────────────────────────────────────────
# One row per (version, directory). Real per-directory values — nothing summed.

df = pd.DataFrame(
    {
        "version": ["v23.1", "v23.1", "v23.2", "v23.2"],
        "directory": ["Derivatives", "Work dir", "Derivatives", "Work dir"],
        "Size": [2.70, 43.0, 0.461, 4.5],
        "File Count": [184, 28000, 126, 6100],
    }
)

palette = {"Derivatives": "#3266ad", "Work dir": "#73b3e0"}

def gb_fmt(x, _=None):
    if x >= 10:
        return f'{x:.0f} GB'
    if x == 0:
        return '0 GB'
    return f'{x:.1f} GB'


def file_fmt(x, _=None):
    return f"{x / 1000:.0f}K" if x >= 1000 else f"{int(x)}"


def make_figure(data, outfile):
    """Two-panel stacked horizontal bars (size | file count) from tidy data."""
    fig, (ax_files, ax_size) = plt.subplots(1, 2, figsize=(10, 1.5))

    for ax, metric, fmt in [
        (ax_size, "Size", gb_fmt),
        (ax_files, "File Count", file_fmt),
    ]:
        (
            so.Plot(data, x=metric, y="version", color="directory")
            .add(so.Bar(width=0.6), so.Stack(), legend=False)
            .scale(color=palette)
            .label(y="")
            .on(ax)
            .plot()
        )
        ax.xaxis.set_major_formatter(mticker.FuncFormatter(fmt))
        sns.despine(ax=ax, left=True, bottom=True)

    # Legend built from the directories actually present in the data
    dirs = data["directory"].unique()
    handles = [Patch(facecolor=palette[d], label=d) for d in dirs]
    fig.legend(
        handles=handles,
        loc="lower center",
        ncol=len(dirs),
        frameon=False,
        fontsize=11,
        bbox_to_anchor=(0.5, -0.06),
    )

    fig.tight_layout(rect=[0, 0.04, 1, 0.96])
    fig.savefig(outfile, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved {outfile}")


make_figure(df[df["directory"] == "Derivatives"], "fit_derivs.png")
make_figure(df, "fit_derivs_and_scratch.png")
