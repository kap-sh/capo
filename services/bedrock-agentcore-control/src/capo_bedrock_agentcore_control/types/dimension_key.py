"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DimensionKey``."""

from typing import TypeAlias

"""<p>A dimension key specifying the scope dimension for rate limiting.</p> <p>Allowed values: <code>targetName</code>, <code>toolName</code>, <code>qualifiedModelId</code>, or trusted context-path expressions: <code>$.context.iam.principal</code>, <code>$.context.iam.sourceIdentity</code>, <code>$.context.jwt.&lt;claim&gt;</code> where <code>&lt;claim&gt;</code> is a JWT claim name (for example, <code>$.context.jwt.sub</code>).</p> <p>For caller-supplied custom context, you can use only fixed field pointers: <code>$.context.request.header.&lt;HTTP-header-name&gt;</code> and <code>$.context.request.body.&lt;simple-dotted-field-path&gt;</code>. These pointers aren't general JSONPath expressions. The server rejects recursion, filters, bracket notation, and wildcards. It also validates each value to enforce allowed prefixes and patterns.</p>"""
DimensionKey: TypeAlias = str
