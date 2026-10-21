# GitHub Recommender for Beginners

**Help newcomers find GitHub repositories that are both popular and actually beginner-friendly.**

Most people sort by stars. For beginners that often fails: a high-star project can be too complex, poorly documented, or missing beginner guides. This tool ranks repositories using a **Learning Score** (documentation quality, beginner content, community activity, etc.) combined with stars (35% stars + 65% Learning Score). Only repos with ≥1,000 stars are considered.

## Features

- Learning-friendly scoring beyond raw star count
- Prioritizes clear documentation and beginner-oriented content
- Considers community activity
- Optional Python news feed from planetpython.org
- Designed for people just starting or exploring a new language/topic

## Installation

```bash
# From source (recommended)
git clone https://github.com/YUBINXIAO/GitHub-Recommender-for-Beginners.git
cd GitHub-Recommender-for-Beginners
pip install -e .
```

Or once published:

```bash
pip install GitHubRecommender
```

## Usage

See the package documentation under `GitHubRecommender/` and the source docs in `GitHubRecommender/source/`.

GitHub API calls read an optional personal access token from the `GITHUB_TOKEN` environment variable. Set it to use the authenticated rate limit. If it is unset, requests are sent with no `Authorization` header and use the lower unauthenticated limit.

```bash
export GITHUB_TOKEN=your_token_here
```

## Maintenance status

This project is under active maintenance again in 2026. Recent work includes documentation refresh, install path fixes, and planning improvements to the scoring model and data pipeline. Issues and contributions are welcome.

## Roadmap

- Refresh the Learning Score weights with more recent repository signals
- Improve data acquisition reliability (rate limits, caching)
- Add simple CLI entry point
- Expand language support beyond Python-focused examples

## License

MIT. See [LICENSE](LICENSE).

---

Originally created as a class project; now maintained to keep helping beginners navigate GitHub.
