"""Generated from Smithy shape ``com.amazonaws.vpclattice#FixedResponseAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.http_status_code


class FixedResponseAction(TypedDict, closed=True):
    status_code: "capo_vpc_lattice.types.http_status_code.HttpStatusCode"
    """<p>The HTTP response code. Only <code>404</code> and <code>500</code> status codes are supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FixedResponseAction) -> dict:
    out: dict = {}
    out["statusCode"] = value["status_code"]
    return out


def deserialize_json(data: dict) -> FixedResponseAction:
    out: FixedResponseAction = {}  # type: ignore[typeddict-item]
    if data.get("statusCode") is not None:
        out["status_code"] = data["statusCode"]
    else:
        out["status_code"] = 0
    return out
