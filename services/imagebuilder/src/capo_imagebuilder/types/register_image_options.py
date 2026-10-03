"""Generated from Smithy shape ``com.amazonaws.imagebuilder#RegisterImageOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.nullable_boolean
    import capo_imagebuilder.types.uefi_data


class RegisterImageOptions(TypedDict, closed=True):
    secure_boot_enabled: NotRequired[
        "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether Secure Boot is enabled for the output AMI. The default value is <code>true</code>. To disable Secure Boot for custom unsigned drivers, set this value to <code>false</code>.</p>"""
    uefi_data: NotRequired["capo_imagebuilder.types.uefi_data.UefiData"]
    """<p>A Base64-encoded representation of the non-volatile UEFI variable store. You can specify this parameter only when <code>secureBootEnabled</code> is <code>true</code> or unspecified. You can inspect and modify the UEFI data by using the <a href="https://github.com/awslabs/python-uefivars">python-uefivars tool on GitHub</a>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/uefi-variables.html">UEFI variables for Amazon EC2 instances</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterImageOptions) -> dict:
    out: dict = {}
    if "secure_boot_enabled" in value:
        out["secureBootEnabled"] = value["secure_boot_enabled"]
    if "uefi_data" in value:
        out["uefiData"] = value["uefi_data"]
    return out


def deserialize_json(data: dict) -> RegisterImageOptions:
    out: RegisterImageOptions = {}  # type: ignore[typeddict-item]
    if data.get("secureBootEnabled") is not None:
        out["secure_boot_enabled"] = data["secureBootEnabled"]
    if data.get("uefiData") is not None:
        out["uefi_data"] = data["uefiData"]
    return out
