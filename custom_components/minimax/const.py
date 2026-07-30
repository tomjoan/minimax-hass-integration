"""Constants for MiniMax integration."""

import logging

from homeassistant.const import Platform

DOMAIN = "minimax"
LOGGER = logging.getLogger(__package__)

DEFAULT_TITLE = "MiniMax"
DEFAULT_CONVERSATION_NAME = "MiniMax Conversation"

PLATFORMS = (
    Platform.CONVERSATION,
    Platform.STT,
    Platform.TTS,
)

MINIMAX_ANTHROPIC_API_URL = "https://api.minimaxi.com/anthropic/v1/messages"
MINIMAX_TTS_API = "https://api.minimaxi.com/v1/t2a_v2"
MINIMAX_STT_API = "https://api.minimaxi.com/v1/audio/transcription"
DEFAULT_STT_NAME = "MiniMax STT"
DEFAULT_TTS_NAME = "MiniMax TTS"

CONF_API_KEY = "api_key"
CONF_RECOMMENDED = "recommended"
CONF_PROMPT = "prompt"
CONF_CHAT_MODEL = "chat_model"
CONF_VOICE_ID = "voice_id"

RECOMMENDED_CHAT_MODEL = "MiniMax-M2.7"
RECOMMENDED_TTS_MODEL = "speech-2.8-hd"
RECOMMENDED_STT_MODEL = "MiniMax-M2.7"

CHAT_MODELS = [
    {"label": "MiniMax-M2.7 (Recommended)", "value": "MiniMax-M2.7"},
    {
        "label": "MiniMax-M2.7-highspeed (Fast)",
        "value": "MiniMax-M2.7-highspeed",
    },
    {"label": "MiniMax-M2.5", "value": "MiniMax-M2.5"},
    {
        "label": "MiniMax-M2.5-highspeed (Fast)",
        "value": "MiniMax-M2.5-highspeed",
    },
    {"label": "MiniMax-M2.1", "value": "MiniMax-M2.1"},
    {
        "label": "MiniMax-M2.1-highspeed (Fast)",
        "value": "MiniMax-M2.1-highspeed",
    },
    {"label": "MiniMax-M2", "value": "MiniMax-M2"},
]


CONF_SPEED = "speed"
CONF_VOL = "vol"
CONF_PITCH = "pitch"
DEFAULT_SPEED = 1.0
DEFAULT_VOL = 1.0
DEFAULT_PITCH = 0

CONF_CONVERSATION_TTS_ENABLED = "conversation_tts_enabled"
DEFAULT_CONVERSATION_TTS_ENABLED = True

CONF_CONVERSATION_MAX_TOKENS = "conversation_max_tokens"
DEFAULT_CONVERSATION_MAX_TOKENS = 16000
DEFAULT_MIN_MAX_TOKENS = 1000

CONF_CONVERSATION_EXPIRY_MINUTES = "conversation_expiry_minutes"
DEFAULT_CONVERSATION_EXPIRY_MINUTES = 5

CONF_MAX_CONVERSATIONS = "max_conversations"
DEFAULT_MAX_CONVERSATIONS = 50

CONF_MEMORY_ENABLED = "memory_enabled"
DEFAULT_MEMORY_ENABLED = True

CONF_MEMORY_MAX_COUNT = "memory_max_count"
DEFAULT_MEMORY_MAX_COUNT = 50

CONF_MEMORY_EXPIRY_DAYS = "memory_expiry_days"
DEFAULT_MEMORY_EXPIRY_DAYS = 30

MEMORY_CATEGORIES = [
    "name",
    "preference",
    "habit",
    "device",
    "other",
]

SUPPORTED_LANGUAGES = ["zh-CN", "en-US"]

VOICE_IDS = {
    "en-US": [
        "English_expressive_narrator",
        "English_radiant_girl",
        "English_magnetic_voiced_man",
        "English_captivating_female1",
        "English_Aussie_Bloke",
        "English_Upbeat_Woman",
        "English_Trustworth_Man",
        "English_CalmWoman",
        "English_UpsetGirl",
        "English_Gentle-voiced_man",
        "English_Whispering_girl",
        "English_Diligent_Man",
        "English_Graceful_Lady",
        "English_ReservedYoungMan",
        "English_PlayfulGirl",
        "English_ManWithDeepVoice",
        "English_MaturePartner",
        "English_CheerfulGirl",
        "English_TeenageBoy",
        "English_AdultBoy",
        "English_LocalYoungMan",
        "English_CasualMan",
        "English_CountryLady",
        "English_MeditativeMan",
        "English_GentleWoman",
        "English_Narrator",
        "English_ThoughtfulMan",
        "English_Orator",
        "English_Robot",
        "English_RomanticMan",
        "English_RelaxedMan",
        "English_StoryWriter",
        "English_MelodiousWoman",
        "English_SunnyBoy",
        "English_HomeBodyDad",
        "English_CheerfulDad",
        "English_LovelyGirl",
        "English_SassyGirl",
        "English_HumorGirl",
        "English_PositiveGirl",
        "English_CalmMan",
        "English_SophisticatedLady",
        "English_ProfessionalMan",
        "English_MagneticWoman",
        "English_Professors_Wife",
        "English_ElderlyMan",
        "English_ClearYouth",
        "English_VivaciousWoman",
        "English_DynamicWoman",
        "English_MatureLady",
        "English_CheerfulMale",
        "English_CalmLady",
        "English_YouthfulMale",
        "English_LocalMan",
        "English_ThoughtfulLady",
        "English_ClearWoman",
    ],
    "zh-CN": [
        "male-qn-qingse",
        "male-qn-jingying",
        "male-qn-badao",
        "male-qn-daxuesheng",
        "female-shaonv",
        "female-yujie",
        "female-chengshu",
        "female-tianmei",
        "male-qn-qingse-jingpin",
        "male-qn-jingying-jingpin",
        "male-qn-badao-jingpin",
        "male-qn-daxuesheng-jingpin",
        "female-shaonv-jingpin",
        "female-yujie-jingpin",
        "female-chengshu-jingpin",
        "female-tianmei-jingpin",
        "clever_boy",
        "cute_boy",
        "lovely_girl",
        "cartoon_pig",
        "bingjiao_didi",
        "junlang_nanyou",
        "chunzhen_xuedi",
        "lengdan_xiongzhang",
        "badao_shaoye",
        "tianxin_xiaoling",
        "qiaopi_mengmei",
        "wumei_yujie",
        "diadia_xuemei",
        "danya_xuejie",
        "Chinese (Mandarin)_Reliable_Executive",
        "Chinese (Mandarin)_News_Anchor",
        "Chinese (Mandarin)_Mature_Woman",
        "Chinese (Mandarin)_Unrestrained_Young_Man",
        "Arrogant_Miss",
        "Robot_Armor",
        "Chinese (Mandarin)_Kind-hearted_Antie",
        "Chinese (Mandarin)_HK_Flight_Attendant",
        "Chinese (Mandarin)_Humorous_Elder",
        "Chinese (Mandarin)_Gentleman",
        "Chinese (Mandarin)_Warm_Bestie",
        "Chinese (Mandarin)_Male_Announcer",
        "Chinese (Mandarin)_Sweet_Lady",
        "Chinese (Mandarin)_Southern_Young_Man",
        "Chinese (Mandarin)_Wise_Women",
        "Chinese (Mandarin)_Gentle_Youth",
        "Chinese (Mandarin)_Warm_Girl",
        "Chinese (Mandarin)_Kind-hearted_Elder",
        "Chinese (Mandarin)_Cute_Spirit",
        "Chinese (Mandarin)_Radio_Host",
        "Chinese (Mandarin)_Lyrical_Voice",
        "Chinese (Mandarin)_Straightforward_Boy",
        "Chinese (Mandarin)_Sincere_Adult",
        "Chinese (Mandarin)_Gentle_Senior",
        "Chinese (Mandarin)_Stubborn_Friend",
        "Chinese (Mandarin)_Crisp_Girl",
        "Chinese (Mandarin)_Pure-hearted_Boy",
        "Chinese (Mandarin)_Soft_Girl",
        "Cantonese_ProfessionalHost（F)",
        "Cantonese_GentleLady",
        "Cantonese_ProfessionalHost（M)",
        "Cantonese_PlayfulMan",
        "Cantonese_CuteGirl",
        "Cantonese_KindWoman",
    ],
}

RECOMMENDED_CONVERSATION_OPTIONS = {
    CONF_PROMPT: "You are EVA, a friendly Danish AI home assistant. You speak Danish. Be warm, direct and practical. Respond briefly and precisely in Danish.",
    CONF_RECOMMENDED: True,
    CONF_CONVERSATION_TTS_ENABLED: DEFAULT_CONVERSATION_TTS_ENABLED,
    CONF_MEMORY_ENABLED: DEFAULT_MEMORY_ENABLED,
    CONF_MEMORY_MAX_COUNT: DEFAULT_MEMORY_MAX_COUNT,
    CONF_MEMORY_EXPIRY_DAYS: DEFAULT_MEMORY_EXPIRY_DAYS,
}

RECOMMENDED_TTS_OPTIONS = {
    CONF_RECOMMENDED: True,
    CONF_VOICE_ID: "English_PlayfulGirl",
    CONF_SPEED: DEFAULT_SPEED,
    CONF_VOL: DEFAULT_VOL,
    CONF_PITCH: DEFAULT_PITCH,
}

RECOMMENDED_STT_OPTIONS = {
    CONF_RECOMMENDED: True,
    CONF_PROMPT: "Transcribe the attached audio",
}
