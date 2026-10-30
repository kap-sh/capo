"""Generated from Smithy shape ``com.amazonaws.continuum#RemoveKubernetesClusterRole``."""

from typing_extensions import TypedDict


class RemoveKubernetesClusterRole(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: RemoveKubernetesClusterRole) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveKubernetesClusterRole:
    out: RemoveKubernetesClusterRole = {}  # type: ignore[typeddict-item]
    return out
