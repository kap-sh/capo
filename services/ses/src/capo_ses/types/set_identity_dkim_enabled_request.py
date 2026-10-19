"""Generated from Smithy shape ``com.amazonaws.ses#SetIdentityDkimEnabledRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.enabled
    import capo_ses.types.identity


class SetIdentityDkimEnabledRequest(TypedDict, closed=True):
    identity: "capo_ses.types.identity.Identity"
    """<p>The identity for which DKIM signing should be enabled or disabled.</p>"""
    dkim_enabled: "capo_ses.types.enabled.Enabled"
    """<p>Sets whether DKIM signing is enabled for an identity. Set to <code>true</code> to enable DKIM signing for this identity; <code>false</code> to disable it. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetIdentityDkimEnabledRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Identity", str(value["identity"])))
    pairs.append(
        (f"{key_prefix}DkimEnabled", "true" if value["dkim_enabled"] else "false")
    )


def deserialize_query(el: Element) -> SetIdentityDkimEnabledRequest:
    out: SetIdentityDkimEnabledRequest = {}  # type: ignore[typeddict-item]
    child_identity = el.find("Identity")
    if child_identity is not None:
        out["identity"] = str(child_identity.text or "")
    else:
        raise DeserializationError("SetIdentityDkimEnabledRequest.identity required")
    child_dkim_enabled = el.find("DkimEnabled")
    if child_dkim_enabled is not None:
        out["dkim_enabled"] = (child_dkim_enabled.text or "").lower() == "true"
    else:
        raise DeserializationError(
            "SetIdentityDkimEnabledRequest.dkim_enabled required"
        )
    return out
