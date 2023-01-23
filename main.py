from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount("/files", StaticFiles(directory="files"), name="files")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("test")
async def test_data():
    return {"EQUIPMENT_CODE": "ABC",
            "EQUIPMENT_ID": 23999,
            "JOB_ID": 3452,
            "JOB_PLAN_ID": 222,
            "LOG_ID": 54234,
            "PDF": "http://localhost:8000/files/report.pdf",
            "VESSEL_OBJECT_ID": 100000,
            "cylinder1":{"Fault_id": 99, "Rating": "0","Recommendation": "(Unacceptable) - Carbon - 1) Replace or Overhaul fuel injector to avoid improper combustion\n 2) Adjust fuel temperature/viscocity to attain correct viscocity as per Maker's recommendation\n 3) Check the condition of piston rings free movement (Gas sealing)\n 4) Adjust the Cylinder Oil Feed rate to avoid over lubrication to avoid formation of carbon deposits\n || (Unacceptable) - Scratch - 1) Adjust the Cylinder Oil Feed rate\n 2) Carry out Drain oil analysis (On board or send ashore)\n 3) Carry out or land samples for Fuel oil analysis\n 4) Check for Hard abrasive particles\n || (Unacceptable) - Carbon - 1) Replace or Overhaul fuel injector to avoid improper combustion\n 2) Adjust fuel temperature/viscocity to attain correct viscocity as per Maker's recommendation\n 3) Check the condition of piston rings free movement (Gas sealing)\n 4) Adjust the Cylinder Oil Feed rate to avoid over lubrication to avoid formation of carbon deposits\n || (Marginal) - Carbon - 1) Replace or Overhaul fuel injector to avoid improper combustion\n 2) Adjust fuel temperature/viscocity to attain correct viscocity as per Maker's recommendation\n 3) Check the condition of piston rings free movement (Gas sealing)\n 4) Adjust the Cylinder Oil Feed rate to avoid over lubrication to avoid formation of carbon deposits"},
            "cylinder2":{"Fault_id": "5", "Rating": "2", "Recommendation": "(Fair) - Carbon - 1) Replace or Overhaul fuel injector to avoid improper combustion\n 2) Adjust fuel temperature/viscocity to attain correct viscocity as per Maker's recommendation\n 3) Check the condition of piston rings free movement (Gas sealing)\n 4) Adjust the Cylinder Oil Feed rate to avoid over lubrication to avoid formation of carbon deposits"},
            "cylinder3":{"Fault_id": "4", "Rating": "1", "Recommendation": "(Marginal) - Collapsed - 1) Replace Piston Rings\n 2) Check for Carbon deposits in the ring groove\n 3) Check vertical ring clearance\n 4) Check for Partial sticking\n 5) Check for Poor sealing between the ring and the ring groove floor.\n 6) Check for Clover leafing \n 7) Check for Ring end chamfers.\n 8) Check for too large ring edge radii.\n 9) Check for Continual striking against wear ridges, or other irregularities in the cylinder wall.\n || (Marginal) - Collapsed - 1) Replace Piston Rings\n 2) Check for Carbon deposits in the ring groove\n 3) Check vertical ring clearance\n 4) Check for Partial sticking\n 5) Check for Poor sealing between the ring and the ring groove floor.\n 6) Check for Clover leafing \n 7) Check for Ring end chamfers.\n 8) Check for too large ring edge radii.\n 9) Check for Continual striking against wear ridges, or other irregularities in the cylinder wall.\n || (Fair) - Collapsed - 1) Replace Piston Rings\n 2) Check for Carbon deposits in the ring groove\n 3) Check vertical ring clearance\n 4) Check for Partial sticking\n 5) Check for Poor sealing between the ring and the ring groove floor.\n 6) Check for Clover leafing \n 7) Check for Ring end chamfers.\n 8) Check for too large ring edge radii.\n 9) Check for Continual striking against wear ridges, or other irregularities in the cylinder wall"},
            "cylinder4":{"Fault_id": 99, "Rating": "0", "Recommendation": "(Unacceptable) - Carbon - 1) Replace or Overhaul fuel injector to avoid improper combustion\n 2) Adjust fuel temperature/viscocity to attain correct viscocity as per Maker's recommendation\n 3) Check the condition of piston rings free movement (Gas sealing)\n 4) Adjust the Cylinder Oil Feed rate to avoid over lubrication to avoid formation of carbon deposits\n || (Unacceptable) - Carbon - 1) Replace or Overhaul fuel injector to avoid improper combustion\n 2) Adjust fuel temperature/viscocity to attain correct viscocity as per Maker's recommendation\n 3) Check the condition of piston rings free movement (Gas sealing)\n 4) Adjust the Cylinder Oil Feed rate to avoid over lubrication to avoid formation of carbon deposits\n || (Fair) - Too Much Oil - 1) Adjust the Cylinder Oil Feed rate\n 2) Carry out Drain oil analysis (On board or send ashore)\n 3) Adjust feed rate to obtain optimum residual BN"}}
