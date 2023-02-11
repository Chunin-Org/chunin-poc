from chunin_poc.common.types import ConfigDict

from .google import profile as google_profile

profiles: dict[str, ConfigDict] = {
    "google": google_profile,
}
