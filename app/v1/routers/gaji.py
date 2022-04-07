from fastapi import APIRouter


router = APIRouter()


@router.post("/setting-pangkat/")
async def setting_pangkat():
    return {}


@router.post("/setting-golongan/")
async def setting_golongan():
    return {}


@router.post("/setting-jabatan/")
async def setting_jabatan():
    return {}


@router.post("/setting-grade/")
async def setting_grade():
    return {}


@router.post("/setting-bpjs/")
async def setting_bpjs():
    return {}


@router.post("/setting-status-kawin/")
async def setting_status_kawin():
    return {}


@router.post("/setting-perjadin/")
async def setting_perjadin():
    return {}


@router.post("/setting-penghasilan/")
async def setting_penghasilan():
    return {}


@router.post("/setting-potongan/")
async def setting_potongan():
    return {}