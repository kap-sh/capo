"""Generated from Smithy shape ``com.amazonaws.opensearch#RetentionAction``."""

from typing import Literal, TypeAlias, cast

"""<p>The action that ends the retention period. <code>RollbackToPrimaryCluster</code> moves the domain back to the primary cluster. <code>DeletePrimaryCluster</code> deletes the primary cluster.</p>"""
RetentionAction: TypeAlias = Literal[
    "RollbackToPrimaryCluster",
    "DeletePrimaryCluster",
]


# --- restJson1 ser/de ---
def serialize_json(value: RetentionAction) -> str:
    return value


def deserialize_json(data: str) -> RetentionAction:
    return cast(RetentionAction, data)
