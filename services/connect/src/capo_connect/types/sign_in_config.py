"""Generated from Smithy shape ``com.amazonaws.connect#SignInConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.sign_in_distribution_list


class SignInConfig(TypedDict, closed=True):
    distributions: "capo_connect.types.sign_in_distribution_list.SignInDistributionList"
    """<p>Information about traffic distributions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SignInConfig) -> dict:
    out: dict = {}
    import capo_connect.types.sign_in_distribution_list

    out["Distributions"] = capo_connect.types.sign_in_distribution_list.serialize_json(
        value["distributions"]
    )
    return out


def deserialize_json(data: dict) -> SignInConfig:
    out: SignInConfig = {}  # type: ignore[typeddict-item]
    if data.get("Distributions") is not None:
        import capo_connect.types.sign_in_distribution_list

        out["distributions"] = (
            capo_connect.types.sign_in_distribution_list.deserialize_json(
                data["Distributions"]
            )
        )
    else:
        out["distributions"] = []
    return out
