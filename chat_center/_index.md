# PKW Chat Center Bundle

This bundle defines the **global chat operating space** for PKW.

It is not a world/place.
It is the system layer that hosts:
- companion presence rules
- session modes
- speaker tag conventions
- chat routing (START_HERE)
- room structure

## Entry points
- [START_HERE.md](START_HERE.md)
- [_meta/_index.md](_meta/_index.md)
- [rooms/_index.md](rooms/_index.md)
- [logs/_index.md](logs/_index.md)

## Scope
Chat Center governs how we work inside ChatGPT:
- how bundles are loaded for a session
- how voices are labeled (speaker tags)
- how to avoid context drift
- how to safely reset a chat
- where different kinds of conversation belongs (rooms)
- how we capture condensed history (logs)

World content (Hollowverse, Forest of Illusions, etc.) lives in world bundles.
