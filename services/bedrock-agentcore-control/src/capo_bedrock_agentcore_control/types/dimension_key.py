"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DimensionKey``."""

from typing import TypeAlias

"""<p>A dimension key specifying the scope dimension for rate limiting.</p> <p>Allowed values: <code>targetName</code>, <code>toolName</code>, <code>qualifiedModelId</code>, or context-path expressions: <code>$.context.iam.principal</code>, <code>$.context.iam.sourceIdentity</code>, <code>$.context.jwt.&lt;claim&gt;</code> where <code>&lt;claim&gt;</code> is a JWT claim name (for example, <code>$.context.jwt.sub</code>). Validated server-side to enforce allowed prefixes and patterns.</p>"""
DimensionKey: TypeAlias = str
