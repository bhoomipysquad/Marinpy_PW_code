from pages.add_new_boat import Add_New_Boat
from pages.claim_marina_flow import Claim_Marina
from pages.profile_edit import Profile_Edit
from pages.super_admin_claim_approved_reject import  Super_Admin_Marina_Claims


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
    claim_approved = Super_Admin_Marina_Claims(admin_page)
    claim_approved.claim_approved_super_admin()

def test_claim_marina_flow(boater_acc_signup):
    page = boater_acc_signup
    claim = Claim_Marina(page)
    claim.claim_marina_flow()

def test_claim_approved_super_admin(super_admin_acc_login):
    page = super_admin_acc_login
    claim_approved = Super_Admin_Marina_Claims(page)
    claim_approved.claim_approved_super_admin()

def test_claim_rejected_super_admin(super_admin_acc_login):
    page = super_admin_acc_login
    claim_reject = Super_Admin_Marina_Claims(page)
    claim_reject.claim_rejected_super_admin()


def test_super_admin_clarification_claim(super_admin_acc_login):
    page = super_admin_acc_login
    claim_clarification = Super_Admin_Marina_Claims(page)
    claim_clarification.claim_needs_clarification()

def test_marina_active_to_inactive(super_admin_acc_login):
    page = super_admin_acc_login
    marina_active_inactive = Super_Admin_Marina_Claims(page)
    marina_active_inactive.marina_active_to_inactive()



def test_booking_flow(boater_acc_login):
    booking_boater = boater_acc_login

