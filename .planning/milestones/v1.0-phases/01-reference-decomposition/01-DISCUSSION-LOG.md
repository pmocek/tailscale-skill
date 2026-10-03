# Phase 1: Reference Decomposition - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-10-02
**Phase:** 1-Reference Decomposition
**Areas discussed:** CLI Partitioning, DERP Relay Scope, tsnet Patterns Boundary, Cross-Reference Convention

---

## CLI Partitioning

### Question 1: How should low-level diagnostic and debugging CLI commands be partitioned from cli.md?
| Option | Selected |
|--------|:--------:|
| Create references/cli-diagnostics.md for deep diagnostic commands (netcheck, ping flags, nc, bugreport, metrics) and keep operational commands in cli.md | ✓ |
| Condense cli.md in-place by trimming verbose explanations and keeping all subcommands in one file | |
| You decide the cleanest partitioning structure | |

### Question 2: Should cli.md retain brief quick-reference entries for basic connectivity checks, or move them exclusively to cli-diagnostics.md?
| Option | Selected |
|--------|:--------:|
| Keep brief 1-line syntax examples for status/ping/netcheck in cli.md with an explicit link to cli-diagnostics.md for advanced flags and workflows | ✓ |
| Completely move all status, ping, netcheck, nc, and bugreport content exclusively to cli-diagnostics.md | |
| You decide what keeps cli.md most operational | |

### Question 3: Where should the "Operating the CLI" agent behavioral guidance and diagnostics flow live?
| Option | Selected |
|--------|:--------:|
| Keep general CLI agent operational rules in cli.md, and move the 4-step "Diagnostics flow" into cli-diagnostics.md | ✓ |
| Keep all agent guidelines (including diagnostics flow) in cli.md and cross-reference from cli-diagnostics.md | |
| Duplicate the relevant agent guidelines in both files | |

### Question 4: How should platform-specific paths and tab completion configurations be handled in cli.md?
| Option | Selected |
|--------|:--------:|
| Keep shell completions and platform locations in cli.md as concise reference snippets | |
| Move shell tab completion configuration to installation.md or common-tasks.md to save budget | ✓ |
| You decide based on budget headroom | |

### Question 5: How should tailscale lock CLI subcommands be represented across cli.md and connectivity.md?
| Option | Selected |
|--------|:--------:|
| Keep basic lock CLI commands in cli.md with a direct pointer to connectivity.md for architecture and key management details | ✓ |
| Move all tailscale lock CLI commands to connectivity.md to keep security operations consolidated | |
| You decide based on token budget | |

### Question 6: How deeply should tailscale serve and funnel examples be documented in cli.md vs sharing-and-publishing.md?
| Option | Selected |
|--------|:--------:|
| Keep essential command syntax in cli.md (port forwarding, web serving) and refer to sharing-and-publishing.md for policy and funnel ACL setup | ✓ |
| Retain full examples in cli.md if token budget permits (target <1,500 tokens for cli.md) | |
| Trim serve and funnel to a 1-line pointer to sharing-and-publishing.md | |

### Question 7: Should network inspection commands (tailscale nc and tailscale dns) move into cli-diagnostics.md?
| Option | Selected |
|--------|:--------:|
| Move tailscale nc and tailscale dns to cli-diagnostics.md alongside ping and netcheck | ✓ |
| Keep tailscale dns in cli.md, but move tailscale nc to cli-diagnostics.md | |
| You decide the cleanest separation | |

### Question 8: Where should specialized admin commands like tailscale configure and tailscale syspolicy live?
| Option | Selected |
|--------|:--------:|
| Keep configure and syspolicy in cli.md under an Administration section with links to containers.md and device-management.md | |
| Move configure kubeconfig to containers.md and syspolicy to device-management.md | ✓ |
| You decide based on budget headroom | |

### Question 9: How should file transfer (Taildrop) and persistent directory sharing (Taildrive) be handled in cli.md?
| Option | Selected |
|--------|:--------:|
| Keep essential cp/get and share/list syntax in cli.md with cross-links to sharing-and-publishing.md | ✓ |
| Move tailscale file and drive completely to sharing-and-publishing.md to maximize CLI budget headroom | |
| You decide based on token budget | |

### Question 10: Where should the tailscale update command documentation live?
| Option | Selected |
|--------|:--------:|
| Keep tailscale update in cli.md under an Administration section | |
| Move tailscale update to installation.md alongside package manager update commands | ✓ |
| You decide based on budget headroom | |

### Question 11: Where should tailscale bugreport and tailscale metrics be placed?
| Option | Selected |
|--------|:--------:|
| Move both tailscale bugreport and tailscale metrics into cli-diagnostics.md | ✓ |
| Move bugreport to cli-diagnostics.md, but keep metrics in cli.md | |
| You decide based on diagnostic cohesion | |

### Question 12: What title and scope definition should be used for the new references/cli-diagnostics.md file?
User write-in: `# Diagnostics and Troubleshooting via CLI`

---

## DERP Relay Scope

### Question 1: Should derp-relays.md cover both Peer Relays and DERP servers, or only DERP servers?
| Option | Selected |
|--------|:--------:|
| Move both Custom DERP maps/servers and Peer Relay configuration into derp-relays.md, leaving the high-level 3-tier mental model in connectivity.md | ✓ |
| Move only Custom DERP maps/servers to derp-relays.md and keep Peer Relay configuration in connectivity.md | |
| You decide based on token headroom and architectural clarity | |

### Question 2: Where should the DERP and Peer Relay external documentation lookup tables live?
| Option | Selected |
|--------|:--------:|
| Move DERP and Peer Relay external doc tables to derp-relays.md, keeping general connectivity doc tables in connectivity.md | ✓ |
| Keep a consolidated documentation table in connectivity.md and cross-reference from derp-relays.md | |
| You decide based on document self-containment | |

### Question 3: How should connectivity.md introduce relays once the configuration details are moved?
| Option | Selected |
|--------|:--------:|
| Retain the 3-tier mental model and NAT matrix in connectivity.md, with an explicit navigation link to derp-relays.md for configuration and deployment | ✓ |
| Extract the entire relay concept and NAT matrix into derp-relays.md, keeping connectivity.md strictly about Tailnet Lock and direct connections | |
| You decide the optimal distribution | |

### Question 4: Should the Remote Desktop (RDP/VNC/RustDesk) and At-Home Access recipes remain in connectivity.md?
| Option | Selected |
|--------|:--------:|
| Keep Remote Desktop and At-home access recipes in connectivity.md (token budget will be well under 1,500 tokens) | |
| Move Remote Desktop to common-tasks.md to keep connectivity.md strictly focused on network transport and security | ✓ |
| You decide based on token budget and coherence | |

### Question 5: What title and scope definition should be used for the new references/derp-relays.md file?
| Option | Selected |
|--------|:--------:|
| "# DERP Relays and Peer Relays" with clear scope on relay architecture, custom DERP maps, and peer relay setup | ✓ |
| "# Tailscale Relay Operations" with scope on DERP servers and node-based relays | |
| You decide the title and introductory scope | |

### Question 6: How should the H1 header of connectivity.md be adjusted to reflect its updated scope?
| Option | Selected |
|--------|:--------:|
| Update H1 to "# Connectivity: Connection Architecture, NAT Traversal, and Tailnet Lock" | ✓ |
| Keep H1 as "# Connectivity" for simplicity | |
| You decide based on document title conventions | |

### Question 7: How prominent should the trade-off comparison between Peer Relays and Custom DERP servers be in derp-relays.md?
| Option | Selected |
|--------|:--------:|
| Place a clear warning callout recommending Peer Relays first over self-hosted DERP servers, citing node-sharing limitations | ✓ |
| Keep the warning inline in the custom DERP map section without callout emphasis | |
| You decide based on operational clarity | |

### Question 8: Should derp-relays.md include a section on verifying relay traffic via CLI diagnostics?
| Option | Selected |
|--------|:--------:|
| Add a concise "Verifying Relay Operation" section cross-referencing netcheck and ping from cli-diagnostics.md | ✓ |
| Keep derp-relays.md purely declarative (configuration and policy only) with no CLI diagnostic cross-references | |
| You decide based on token budget | |

---

## tsnet Patterns Boundary

### Question 1: Where should the boundary lie between core tsnet.md and tsnet-patterns.md?
| Option | Selected |
|--------|:--------:|
| tsnet.md holds Server lifecycle, AuthKey/OAuth/OIDC, and basic Listen; tsnet-patterns.md holds Tailscale Services (ListenService), Reverse Proxies, CapMap authorization, and SSH/Funnel listeners | ✓ |
| Keep all listener types in tsnet.md and move only code examples longer than 20 lines to tsnet-patterns.md | |
| You decide the cleanest separation for Go developers | |

### Question 2: How should policy grants and application authorization be partitioned between tsnet.md and tsnet-patterns.md?
| Option | Selected |
|--------|:--------:|
| Keep basic tag/network grants in tsnet.md; move application capability grants (CapMap, UnmarshalCapJSON) to tsnet-patterns.md | ✓ |
| Move all tailnet policy examples (both network and application grants) to tsnet-patterns.md | |
| You decide based on token budget and coherence | |

### Question 3: Where should the tsnet production checklist and best practices guide reside?
| Option | Selected |
|--------|:--------:|
| Retain the core production checklist in tsnet.md, and include pattern-specific production considerations in tsnet-patterns.md | ✓ |
| Move the production checklist entirely to tsnet-patterns.md | |
| You decide based on checklist relevance | |

### Question 4: What title and scope definition should be used for references/tsnet-patterns.md?
| Option | Selected |
|--------|:--------:|
| "# tsnet Advanced Architectural Patterns" covering Services, Reverse Proxies, CapMap, and Multi-protocol listeners | ✓ |
| "# tsnet Patterns and Production Recipes" focusing on implementation recipes | |
| You decide the document heading and scope | |

---

## Cross-Reference Convention

### Question 1: How should split sister documents reference each other for agent navigation?
| Option | Selected |
|--------|:--------:|
| Include a prominent blockquote banner under H1 (e.g. "> **Sister reference:** For ... see [filename](file.md)") plus inline links where topics diverge | ✓ |
| Only include inline relative markdown links at the relevant sections without top banners | |
| Include a standardized "Related References" table at the bottom of each file | |

### Question 2: What relative path format should be used for cross-reference links between sister files inside references/?
| Option | Selected |
|--------|:--------:|
| Use direct sibling relative links [doc.md](doc.md) or [doc.md](./doc.md) within references/ so agents opening a file can resolve relative paths seamlessly | ✓ |
| Always reference from the skill root like [doc.md](references/doc.md) | |
| You decide based on agentskills.io and markdown parser standards | |

### Question 3: What target token ceiling should the planner and executor aim for during decomposition?
| Option | Selected |
|--------|:--------:|
| Target ≤1,500 tokens (~25% safety headroom) for each decomposed file to safely absorb future edits | ✓ |
| Target ≤1,800 tokens (10% safety headroom) to keep files as comprehensive as possible | |
| Strictly enforce the 2,000 token limit without an artificial lower target | |

### Question 4: How strictly should existing code snippets and JSON examples be preserved during file splitting?
| Option | Selected |
|--------|:--------:|
| Preserve all functional code snippets, JSON grants, and CLI examples verbatim across the split files with zero loss of operational examples | |
| Condense or remove redundant comments from code snippets to save additional token budget | ✓ |
| You decide based on budget constraints per file | |

---

## the agent's Discretion

None — all decisions were explicitly guided and resolved.

## Deferred Ideas

None — discussion remained strictly within the scope of Phase 1 reference decomposition.
