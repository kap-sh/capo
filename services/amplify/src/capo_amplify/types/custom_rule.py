"""Generated from Smithy shape ``com.amazonaws.amplify#CustomRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.condition
    import capo_amplify.types.source
    import capo_amplify.types.status
    import capo_amplify.types.target


class CustomRule(TypedDict, closed=True):
    source: "capo_amplify.types.source.Source"
    """<p>The source pattern for a URL rewrite or redirect rule. </p>"""
    target: "capo_amplify.types.target.Target"
    """<p>The target pattern for a URL rewrite or redirect rule. </p>"""
    status: NotRequired["capo_amplify.types.status.Status"]
    """<p>The status code for a URL rewrite or redirect rule. </p> <dl> <dt>200</dt> <dd> <p>Represents a 200 rewrite rule.</p> </dd> <dt>301</dt> <dd> <p>Represents a 301 (moved permanently) redirect rule. This and all future requests should be directed to the target URL. </p> </dd> <dt>302</dt> <dd> <p>Represents a 302 temporary redirect rule.</p> </dd> <dt>404</dt> <dd> <p>Represents a 404 redirect rule.</p> </dd> <dt>404-200</dt> <dd> <p>Represents a 404 rewrite rule.</p> </dd> </dl>"""
    condition: NotRequired["capo_amplify.types.condition.Condition"]
    """<p>The condition for a URL rewrite or redirect rule, such as a country code. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomRule) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    out["target"] = value["target"]
    if "status" in value:
        out["status"] = value["status"]
    if "condition" in value:
        out["condition"] = value["condition"]
    return out


def deserialize_json(data: dict) -> CustomRule:
    out: CustomRule = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        out["source"] = ""
    if data.get("target") is not None:
        out["target"] = data["target"]
    else:
        out["target"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("condition") is not None:
        out["condition"] = data["condition"]
    return out
