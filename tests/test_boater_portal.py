from pages.add_new_boat import Add_New_Boat
from pages.claim_marina_flow import Claim_Marina
from pages.profile_edit import Profile_Edit
from pages.super_admin_claim_approved_reject import Super_Admin_claim_Approved


def test_profile_edit(boater_acc_signup):
    page = boater_acc_signup
    profile_edit = Profile_Edit(page)
    profile_edit.add_profile_info()

def test_add_new_boat(boater_acc_login):
    page = boater_acc_login
    add_boat = Add_New_Boat(page)
    add_boat.add_new_boat()


def test_claim_marina_flow_to_booking_flow(boater_acc_signup, super_admin_acc_login):
    boater_page = boater_acc_signup
    claim = Claim_Marina(boater_page)
    claim.claim_marina_flow()
    admin_page = super_admin_acc_login
    claim_approved = Super_Admin_claim_Approved(admin_page)
    claim_approved.claim_approved_super_admin()

def test_claim_marina_flow(boater_acc_signup):
    page = boater_acc_signup
    claim = Claim_Marina(page)
    claim.claim_marina_flow()

def test_super_admin_approved_claim(super_admin_acc_login):
    page = super_admin_acc_login
    claim_approved = Super_Admin_claim_Approved(page)
    claim_approved.claim_approved_super_admin()

def test_booking_flow(boater_acc_login):
    booking_boater = boater_acc_login


