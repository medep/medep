package org.euvsvirus.connector;

import org.springframework.stereotype.Component;

@Component
public class UpperManagementSystemConnector implements HospitalInformationSystem {

	boolean connected = false;

	@Override
	public void connect() {
		connected = true;
	}

	@Override
	public String whoami() {
		return "I am Upper management system connector. I connect to analytics dashboards of upper/middle management and collect overall KPIs and aggregated and processed data from data warehouses etc.";
	}

	@Override
	public boolean isConnected() {
		return connected;
	}
}
