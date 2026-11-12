<template>
	<div class="min-h-screen bg-slate-900 text-slate-100 flex flex-col font-sans selection:bg-indigo-500 selection:text-white">
		<!-- Top Navigation Bar -->
		<header class="sticky top-0 z-40 backdrop-blur-xl bg-slate-900/80 border-b border-slate-800/80 transition-all">
			<div class="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
				<!-- Brand Logo -->
				<div class="flex items-center space-x-3 cursor-pointer" @click="scrollToTop">
					<div class="h-11 w-11 rounded-xl bg-gradient-to-tr from-violet-600 via-indigo-500 to-cyan-400 p-0.5 shadow-lg shadow-indigo-500/25 flex items-center justify-center">
						<div class="h-full w-full bg-slate-950 rounded-[10px] flex items-center justify-center">
							<span class="text-2xl font-black bg-gradient-to-tr from-violet-400 to-indigo-200 bg-clip-text text-transparent">E</span>
						</div>
					</div>
					<div class="flex flex-col">
						<div class="flex items-center space-x-2">
							<span class="text-2xl font-extrabold tracking-tight text-white">Eliza</span>
							<span class="px-2 py-0.5 text-[10px] font-bold uppercase tracking-wider bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 rounded-full">SaaS</span>
						</div>
						<span class="text-[11px] font-medium text-slate-400 tracking-wide">Modern HR & Payroll</span>
					</div>
				</div>

				<!-- Desktop Nav Links -->
				<nav class="hidden md:flex items-center space-x-8 text-sm font-medium text-slate-300">
					<a href="#features" class="hover:text-white transition">Features</a>
					<a href="#preview" class="hover:text-white transition">Platform</a>
					<a href="#pricing" class="hover:text-white transition">Pricing</a>
					<a href="#architecture" class="hover:text-white transition">Architecture</a>
					<a href="#faq" class="hover:text-white transition">FAQ</a>
				</nav>

				<!-- Quick Access & CTA -->
				<div class="flex items-center space-x-3">
					<a
						href="http://127.0.0.1:8080"
						target="_blank"
						class="hidden sm:inline-flex items-center px-3.5 py-2 text-xs font-semibold rounded-lg text-slate-300 bg-slate-800 hover:bg-slate-700/80 border border-slate-700 transition"
						title="Open Employee Mobile Self-Service PWA"
					>
						<svg class="w-4 h-4 mr-1.5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
						</svg>
						Employee PWA
					</a>

					<router-link
						to="/desk/hr-setup"
						class="hidden sm:inline-flex items-center px-3.5 py-2 text-xs font-semibold rounded-lg text-slate-300 bg-slate-800 hover:bg-slate-700/80 border border-slate-700 transition"
					>
						<svg class="w-4 h-4 mr-1.5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17V7m0 10a2 2 0 01-2 2H5a2 2 0 01-2-2V7a2 2 0 012-2h2a2 2 0 012 2m0 10a2 2 0 002 2h2a2 2 0 002-2M9 7a2 2 0 012-2h2a2 2 0 012 2m0 10V7m0 10a2 2 0 002 2h2a2 2 0 002-2V7a2 2 0 00-2-2h-2a2 2 0 00-2 2" />
						</svg>
						HR Desk
					</router-link>

					<button
						@click="openModal('Growth')"
						class="inline-flex items-center px-4 py-2 text-xs font-bold rounded-lg text-white bg-gradient-to-r from-violet-600 to-indigo-600 hover:from-violet-500 hover:to-indigo-500 shadow-md shadow-indigo-600/30 transition transform hover:-translate-y-0.5"
					>
						Start Free Trial
					</button>
				</div>
			</div>
		</header>

		<!-- Hero Section -->
		<section class="relative pt-16 pb-20 overflow-hidden">
			<!-- Background Glow Orbs -->
			<div class="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[700px] h-[350px] bg-indigo-600/20 rounded-full blur-[120px] pointer-events-none"></div>
			<div class="absolute top-1/3 left-1/4 w-[400px] h-[250px] bg-violet-600/20 rounded-full blur-[100px] pointer-events-none"></div>

			<div class="max-w-7xl mx-auto px-6 relative z-10 text-center">
				<!-- Announcement Pill -->
				<div class="inline-flex items-center space-x-2 px-4 py-1.5 rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-300 text-xs font-medium mb-8">
					<span class="flex h-2 w-2 rounded-full bg-emerald-400 animate-pulse"></span>
					<span>Eliza 2.0 Live</span>
					<span class="text-slate-500">•</span>
					<span>Autonomous Multi-Tenant HR & Payroll</span>
				</div>

				<!-- Main Headline -->
				<h1 class="text-4xl sm:text-6xl lg:text-7xl font-extrabold tracking-tight text-white max-w-5xl mx-auto leading-[1.12]">
					Modern HR, Rostering & Payroll.<br />
					<span class="bg-gradient-to-r from-violet-400 via-indigo-300 to-cyan-300 bg-clip-text text-transparent">
						Engineered for Ambitious Teams.
					</span>
				</h1>

				<!-- Subtitle -->
				<p class="mt-6 text-lg sm:text-xl text-slate-300 max-w-3xl mx-auto leading-relaxed">
					Say goodbye to fragmented spreadsheets and legacy portals. Eliza empowers company leads to automate employee onboarding, shift schedules, leave requests, and payroll in one unified workspace.
					<strong class="text-white font-semibold"> The employer pays one predictable subscription — 100% free for all employees.</strong>
				</p>

				<!-- CTA Buttons -->
				<div class="mt-10 flex flex-col sm:flex-row items-center justify-center gap-4">
					<button
						@click="openModal('Growth')"
						class="w-full sm:w-auto inline-flex items-center justify-center px-8 py-3.5 text-sm font-bold rounded-xl text-white bg-gradient-to-r from-violet-600 via-indigo-600 to-cyan-600 hover:opacity-95 shadow-xl shadow-indigo-600/25 transition transform hover:-translate-y-0.5"
					>
						<span>Start 14-Day Free Trial</span>
						<svg class="ml-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
						</svg>
					</button>

					<router-link
						to="/desk/hr-setup"
						class="w-full sm:w-auto inline-flex items-center justify-center px-6 py-3.5 text-sm font-semibold rounded-xl text-slate-200 bg-slate-800/80 hover:bg-slate-700/80 border border-slate-700 transition"
					>
						<svg class="mr-2 w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
						</svg>
						Explore HR Workspace
					</router-link>

					<a
						href="http://127.0.0.1:8080"
						target="_blank"
						class="w-full sm:w-auto inline-flex items-center justify-center px-6 py-3.5 text-sm font-semibold rounded-xl text-slate-200 bg-slate-800/80 hover:bg-slate-700/80 border border-slate-700 transition"
					>
						<svg class="mr-2 w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
						</svg>
						Launch Employee Mobile PWA
					</a>
				</div>

				<!-- Value Badges -->
				<div class="mt-12 pt-8 border-t border-slate-800/80 max-w-4xl mx-auto grid grid-cols-2 sm:grid-cols-4 gap-6 text-slate-400 text-xs font-medium">
					<div class="flex items-center justify-center space-x-2">
						<svg class="w-4 h-4 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
						</svg>
						<span>PostgreSQL Cloud DB</span>
					</div>
					<div class="flex items-center justify-center space-x-2">
						<svg class="w-4 h-4 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
						</svg>
						<span>Instant 60s Onboarding</span>
					</div>
					<div class="flex items-center justify-center space-x-2">
						<svg class="w-4 h-4 text-cyan-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z" />
						</svg>
						<span>Free Employee Access</span>
					</div>
					<div class="flex items-center justify-center space-x-2">
						<svg class="w-4 h-4 text-violet-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
						</svg>
						<span>Multi-Tenant Partitioned</span>
					</div>
				</div>
			</div>
		</section>

		<!-- Interactive Hero Preview / Live Mockup -->
		<section id="preview" class="max-w-7xl mx-auto px-6 pb-24">
			<div class="rounded-2xl bg-gradient-to-b from-slate-800 to-slate-900 border border-slate-700 shadow-2xl p-4 sm:p-6 lg:p-8">
				<!-- Window Controls Bar -->
				<div class="flex flex-col sm:flex-row sm:items-center justify-between pb-6 border-b border-slate-800 gap-4">
					<div class="flex items-center space-x-3">
						<div class="flex space-x-1.5">
							<div class="w-3 h-3 rounded-full bg-rose-500/80"></div>
							<div class="w-3 h-3 rounded-full bg-amber-500/80"></div>
							<div class="w-3 h-3 rounded-full bg-emerald-500/80"></div>
						</div>
						<div class="h-4 w-px bg-slate-700"></div>
						<span class="text-xs font-mono text-slate-400">eliza.cloud/workspace • Acme Corporation</span>
						<span class="px-2 py-0.5 text-[10px] font-bold rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">GROWTH TIER</span>
					</div>

					<!-- Preview Tabs -->
					<div class="flex items-center space-x-1 bg-slate-950/60 p-1 rounded-lg border border-slate-800 text-xs">
						<button
							v-for="tab in previewTabs"
							:key="tab.id"
							@click="activePreviewTab = tab.id"
							:class="activePreviewTab === tab.id ? 'bg-indigo-600 text-white font-semibold' : 'text-slate-400 hover:text-white'"
							class="px-3 py-1.5 rounded-md transition"
						>
							{{ tab.name }}
						</button>
					</div>
				</div>

				<!-- Live Preview KPI Row -->
				<div class="grid grid-cols-2 lg:grid-cols-4 gap-4 my-6">
					<div class="bg-slate-950/50 p-4 rounded-xl border border-slate-800">
						<p class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">Active Employees</p>
						<p class="text-2xl font-bold text-white mt-1">5 / 50 <span class="text-xs text-indigo-400 font-normal">seats</span></p>
						<div class="w-full bg-slate-800 h-1.5 rounded-full mt-2 overflow-hidden">
							<div class="bg-indigo-500 h-full rounded-full" style="width: 10%"></div>
						</div>
					</div>

					<div class="bg-slate-950/50 p-4 rounded-xl border border-slate-800">
						<p class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">Checked In Today</p>
						<p class="text-2xl font-bold text-emerald-400 mt-1">4 <span class="text-xs text-slate-400 font-normal">(80% on shift)</span></p>
						<p class="text-[11px] text-slate-500 mt-2">● Real-time geo-verified</p>
					</div>

					<div class="bg-slate-950/50 p-4 rounded-xl border border-slate-800">
						<p class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">Pending Leaves</p>
						<p class="text-2xl font-bold text-amber-400 mt-1">2 <span class="text-xs text-slate-400 font-normal">awaiting review</span></p>
						<p class="text-[11px] text-slate-500 mt-2">Annual & Sick leave</p>
					</div>

					<div class="bg-slate-950/50 p-4 rounded-xl border border-slate-800">
						<p class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">Monthly Payroll</p>
						<p class="text-2xl font-bold text-cyan-400 mt-1">$23,500 <span class="text-xs text-slate-400 font-normal">processed</span></p>
						<p class="text-[11px] text-slate-500 mt-2">Slips distributed</p>
					</div>
				</div>

				<!-- Tab Content Showcase -->
				<div class="bg-slate-950/70 rounded-xl border border-slate-800 p-5 min-h-[300px]">
					<!-- Tab 1: Shift Rostering -->
					<div v-if="activePreviewTab === 'shifts'" class="space-y-4">
						<div class="flex items-center justify-between">
							<h4 class="text-sm font-semibold text-slate-200">Weekly Shift Coverage & Allocation</h4>
							<router-link to="/roster" class="text-xs text-indigo-400 hover:text-indigo-300 font-medium flex items-center">
								Open Full Calendar &rarr;
							</router-link>
						</div>
						<div class="grid grid-cols-1 md:grid-cols-3 gap-3">
							<div class="bg-slate-900 p-3.5 rounded-lg border border-slate-800">
								<div class="flex items-center justify-between">
									<span class="text-xs font-bold text-indigo-400 uppercase">Morning Shift</span>
									<span class="text-[11px] text-slate-400">08:00 - 16:30</span>
								</div>
								<p class="text-sm font-medium text-slate-200 mt-2">Engineering & Product</p>
								<div class="mt-3 flex items-center space-x-2">
									<span class="h-6 w-6 rounded-full bg-violet-600 flex items-center justify-center text-[10px] font-bold">JD</span>
									<span class="h-6 w-6 rounded-full bg-blue-600 flex items-center justify-center text-[10px] font-bold">AS</span>
									<span class="text-xs text-slate-400">+2 more</span>
								</div>
							</div>
							<div class="bg-slate-900 p-3.5 rounded-lg border border-slate-800">
								<div class="flex items-center justify-between">
									<span class="text-xs font-bold text-emerald-400 uppercase">General Shift</span>
									<span class="text-[11px] text-slate-400">09:00 - 18:00</span>
								</div>
								<p class="text-sm font-medium text-slate-200 mt-2">Operations & HR Lead</p>
								<div class="mt-3 flex items-center space-x-2">
									<span class="h-6 w-6 rounded-full bg-emerald-600 flex items-center justify-center text-[10px] font-bold">AD</span>
									<span class="text-xs text-slate-400">Administrator</span>
								</div>
							</div>
							<div class="bg-slate-900 p-3.5 rounded-lg border border-slate-800">
								<div class="flex items-center justify-between">
									<span class="text-xs font-bold text-amber-400 uppercase">Evening Support</span>
									<span class="text-[11px] text-slate-400">16:00 - 00:00</span>
								</div>
								<p class="text-sm font-medium text-slate-200 mt-2">Customer Success</p>
								<div class="mt-3 flex items-center space-x-2">
									<span class="h-6 w-6 rounded-full bg-purple-600 flex items-center justify-center text-[10px] font-bold">MR</span>
									<span class="text-xs text-slate-400">1 active</span>
								</div>
							</div>
						</div>
					</div>

					<!-- Tab 2: Employee Directory -->
					<div v-else-if="activePreviewTab === 'employees'" class="space-y-4">
						<div class="flex items-center justify-between">
							<h4 class="text-sm font-semibold text-slate-200">Live Team Roster (Neon PostgreSQL)</h4>
							<router-link to="/desk/hr-setup" class="text-xs text-indigo-400 hover:text-indigo-300 font-medium flex items-center">
								Manage in HR Desk &rarr;
							</router-link>
						</div>
						<div class="overflow-x-auto">
							<table class="w-full text-left text-xs">
								<thead>
									<tr class="text-slate-400 border-b border-slate-800">
										<th class="py-2.5 px-3">Employee</th>
										<th class="py-2.5 px-3">Department</th>
										<th class="py-2.5 px-3">Designation</th>
										<th class="py-2.5 px-3">Role</th>
										<th class="py-2.5 px-3">Status</th>
									</tr>
								</thead>
								<tbody class="divide-y divide-slate-800/60 text-slate-300">
									<tr>
										<td class="py-2.5 px-3 font-medium text-white flex items-center space-x-2">
											<span class="h-6 w-6 rounded-full bg-indigo-600 flex items-center justify-center text-[10px] font-bold">JD</span>
											<span>John Doe</span>
										</td>
										<td class="py-2.5 px-3">Engineering</td>
										<td class="py-2.5 px-3">Senior Software Engineer</td>
										<td class="py-2.5 px-3"><span class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">Employee</span></td>
										<td class="py-2.5 px-3"><span class="text-emerald-400 font-medium">● Active</span></td>
									</tr>
									<tr>
										<td class="py-2.5 px-3 font-medium text-white flex items-center space-x-2">
											<span class="h-6 w-6 rounded-full bg-purple-600 flex items-center justify-center text-[10px] font-bold">JS</span>
											<span>Jane Smith</span>
										</td>
										<td class="py-2.5 px-3">Human Resources</td>
										<td class="py-2.5 px-3">HR Manager</td>
										<td class="py-2.5 px-3"><span class="px-2 py-0.5 rounded bg-indigo-900/50 text-indigo-300 font-medium">HR Lead</span></td>
										<td class="py-2.5 px-3"><span class="text-emerald-400 font-medium">● Active</span></td>
									</tr>
									<tr>
										<td class="py-2.5 px-3 font-medium text-white flex items-center space-x-2">
											<span class="h-6 w-6 rounded-full bg-cyan-600 flex items-center justify-center text-[10px] font-bold">AS</span>
											<span>Alice Smith</span>
										</td>
										<td class="py-2.5 px-3">Product Design</td>
										<td class="py-2.5 px-3">Lead Product Designer</td>
										<td class="py-2.5 px-3"><span class="px-2 py-0.5 rounded bg-slate-800 text-slate-300">Employee</span></td>
										<td class="py-2.5 px-3"><span class="text-emerald-400 font-medium">● Active</span></td>
									</tr>
								</tbody>
							</table>
						</div>
					</div>

					<!-- Tab 3: Attendance -->
					<div v-else-if="activePreviewTab === 'attendance'" class="space-y-4">
						<div class="flex items-center justify-between">
							<h4 class="text-sm font-semibold text-slate-200">Real-Time Mobile Geofence Check-ins</h4>
							<a href="http://127.0.0.1:8080" target="_blank" class="text-xs text-indigo-400 hover:text-indigo-300 font-medium flex items-center">
								Simulate on Mobile PWA &rarr;
							</a>
						</div>
						<div class="space-y-2.5">
							<div class="bg-slate-900/90 p-3 rounded-lg border border-slate-800 flex items-center justify-between text-xs">
								<div class="flex items-center space-x-3">
									<span class="p-1.5 rounded-md bg-emerald-500/10 text-emerald-400">
										<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
											<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1" />
										</svg>
									</span>
									<div>
										<p class="font-medium text-white">John Doe • IN</p>
										<p class="text-[11px] text-slate-400">HQ Office Geofence (40.7128, -74.0060)</p>
									</div>
								</div>
								<div class="text-right">
									<p class="font-mono text-slate-300">08:58 AM</p>
									<span class="text-[10px] text-emerald-400 font-medium">On Time</span>
								</div>
							</div>

							<div class="bg-slate-900/90 p-3 rounded-lg border border-slate-800 flex items-center justify-between text-xs">
								<div class="flex items-center space-x-3">
									<span class="p-1.5 rounded-md bg-emerald-500/10 text-emerald-400">
										<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
											<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1" />
										</svg>
									</span>
									<div>
										<p class="font-medium text-white">Alice Smith • IN</p>
										<p class="text-[11px] text-slate-400">Remote Work (IP Verified)</p>
									</div>
								</div>
								<div class="text-right">
									<p class="font-mono text-slate-300">09:02 AM</p>
									<span class="text-[10px] text-emerald-400 font-medium">On Time</span>
								</div>
							</div>
						</div>
					</div>

					<!-- Tab 4: Payroll -->
					<div v-else class="space-y-4">
						<div class="flex items-center justify-between">
							<h4 class="text-sm font-semibold text-slate-200">Automated Payroll Calculation & Salary Slips</h4>
							<span class="text-xs text-emerald-400 font-medium">Cycle: March 2026 (Completed)</span>
						</div>
						<div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
							<div class="bg-slate-900 p-3.5 rounded-lg border border-slate-800">
								<div class="flex justify-between items-center text-slate-400">
									<span>Base Gross Salary</span>
									<span class="font-semibold text-white">$27,500.00</span>
								</div>
								<div class="flex justify-between items-center text-slate-400 mt-1.5">
									<span>Tax & Benefit Deductions</span>
									<span class="font-semibold text-rose-400">-$4,000.00</span>
								</div>
								<div class="h-px bg-slate-800 my-2"></div>
								<div class="flex justify-between items-center">
									<span class="font-bold text-white">Net Disbursed</span>
									<span class="font-bold text-emerald-400 text-sm">$23,500.00</span>
								</div>
							</div>
							<div class="bg-slate-900 p-3.5 rounded-lg border border-slate-800 flex flex-col justify-between">
								<div>
									<p class="font-medium text-white">Payslips Ready for Download</p>
									<p class="text-slate-400 text-[11px] mt-1">Available instantly on employee mobile self-service app.</p>
								</div>
								<div class="mt-3 flex space-x-2">
									<button class="px-3 py-1.5 rounded bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-[11px]">
										Download Batch PDF
									</button>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>

		<!-- Features Grid ("Why Eliza") -->
		<section id="features" class="py-20 bg-slate-950/60 border-t border-slate-800">
			<div class="max-w-7xl mx-auto px-6">
				<div class="text-center max-w-3xl mx-auto">
					<h2 class="text-xs font-bold uppercase tracking-wider text-indigo-400">Everything Your Company Needs</h2>
					<p class="mt-2 text-3xl sm:text-4xl font-extrabold text-white">A Single Operating System for People & Payroll</p>
					<p class="mt-4 text-slate-400 text-base">
						Built for modern companies who need speed, compliance, and crystal clear multi-tenancy.
					</p>
				</div>

				<div class="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8">
					<!-- Feature 1 -->
					<div class="bg-slate-900 p-8 rounded-2xl border border-slate-800 hover:border-slate-700 transition">
						<div class="h-12 w-12 rounded-xl bg-violet-600/10 text-violet-400 flex items-center justify-center mb-6">
							<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
							</svg>
						</div>
						<h3 class="text-xl font-bold text-white">Multi-Tenant Company Workspace</h3>
						<p class="mt-3 text-sm text-slate-400 leading-relaxed">
							Dedicated company tenant partitions inside Neon PostgreSQL. Your team data, payroll ledgers, and policies are completely isolated and secured.
						</p>
						<ul class="mt-4 space-y-2 text-xs text-slate-300">
							<li class="flex items-center space-x-2">
								<span class="text-emerald-400">✓</span>
								<span>Row-Level Security & Custom Slugs</span>
							</li>
							<li class="flex items-center space-x-2">
								<span class="text-emerald-400">✓</span>
								<span>Configurable Departments & Designations</span>
							</li>
							<li class="flex items-center space-x-2">
								<span class="text-emerald-400">✓</span>
								<span>Real-time DB synchronization</span>
							</li>
						</ul>
					</div>

					<!-- Feature 2 -->
					<div class="bg-slate-900 p-8 rounded-2xl border border-slate-800 hover:border-slate-700 transition">
						<div class="h-12 w-12 rounded-xl bg-indigo-600/10 text-indigo-400 flex items-center justify-center mb-6">
							<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
							</svg>
						</div>
						<h3 class="text-xl font-bold text-white">Free Employee Self-Service PWA</h3>
						<p class="mt-3 text-sm text-slate-400 leading-relaxed">
							Employees check-in with one tap, view shifts, request time off, and download salary slips right from their phones. Zero software fees for employees.
						</p>
						<ul class="mt-4 space-y-2 text-xs text-slate-300">
							<li class="flex items-center space-x-2">
								<span class="text-emerald-400">✓</span>
								<span>Geofenced Clock-in / Clock-out</span>
							</li>
							<li class="flex items-center space-x-2">
								<span class="text-emerald-400">✓</span>
								<span>Instant Leave Balance & Status</span>
							</li>
							<li class="flex items-center space-x-2">
								<span class="text-emerald-400">✓</span>
								<span>Expense receipt claims & approvals</span>
							</li>
						</ul>
					</div>

					<!-- Feature 3 -->
					<div class="bg-slate-900 p-8 rounded-2xl border border-slate-800 hover:border-slate-700 transition">
						<div class="h-12 w-12 rounded-xl bg-cyan-600/10 text-cyan-400 flex items-center justify-center mb-6">
							<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
							</svg>
						</div>
						<h3 class="text-xl font-bold text-white">Automated Payroll & Slips</h3>
						<p class="mt-3 text-sm text-slate-400 leading-relaxed">
							Generate salary slips in one click. Eliza automatically calculates hours from check-in logs, applies statutory tax rules, and distributes PDF slips.
						</p>
						<ul class="mt-4 space-y-2 text-xs text-slate-300">
							<li class="flex items-center space-x-2">
								<span class="text-emerald-400">✓</span>
								<span>One-Click Monthly Run</span>
							</li>
							<li class="flex items-center space-x-2">
								<span class="text-emerald-400">✓</span>
								<span>Dynamic Deductions & Allowances</span>
							</li>
							<li class="flex items-center space-x-2">
								<span class="text-emerald-400">✓</span>
								<span>Direct Bank Disbursal Exports</span>
							</li>
						</ul>
					</div>
				</div>
			</div>
		</section>

		<!-- Interactive ROI & Plan Calculator -->
		<section class="py-16 max-w-5xl mx-auto px-6 w-full">
			<div class="bg-gradient-to-r from-indigo-900/40 via-purple-900/30 to-slate-900 p-8 rounded-2xl border border-indigo-500/20 shadow-xl">
				<div class="flex flex-col md:flex-row items-center justify-between gap-8">
					<div class="space-y-3 max-w-md">
						<span class="px-2.5 py-1 text-xs font-bold rounded-full bg-indigo-500/10 text-indigo-300 border border-indigo-500/30 uppercase">Interactive Calculator</span>
						<h3 class="text-2xl font-bold text-white">How big is your team?</h3>
						<p class="text-sm text-slate-300">
							Move the slider to see which Eliza plan fits your company and the estimated HR hours you'll save each month.
						</p>

						<!-- Team Slider -->
						<div class="pt-4 space-y-2">
							<div class="flex justify-between text-xs font-semibold">
								<span class="text-slate-400">Team Size:</span>
								<span class="text-indigo-400 font-mono text-base font-bold">{{ teamSize }} Employees</span>
							</div>
							<input
								type="range"
								min="5"
								max="150"
								step="5"
								v-model.number="teamSize"
								class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-indigo-500"
							/>
						</div>
					</div>

					<div class="bg-slate-950/80 p-6 rounded-xl border border-slate-800 text-center sm:text-left flex flex-col justify-between w-full md:w-72">
						<div>
							<p class="text-xs font-semibold text-slate-400 uppercase">Recommended Plan</p>
							<p class="text-2xl font-bold text-white mt-1">{{ calculatedPlan.name }}</p>
							<p class="text-indigo-400 text-lg font-bold mt-1">${{ calculatedPlan.price }} <span class="text-xs text-slate-400 font-normal">/ month</span></p>
							<div class="mt-4 pt-4 border-t border-slate-800 text-xs text-slate-300 space-y-1">
								<p>⚡ Saves <strong class="text-emerald-400">{{ calculatedHoursSaved }} hrs</strong> / month</p>
								<p>👥 Free employee mobile app</p>
							</div>
						</div>
						<button
							@click="openModal(calculatedPlan.name)"
							class="mt-5 w-full py-2.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs shadow transition"
						>
							Select {{ calculatedPlan.name }}
						</button>
					</div>
				</div>
			</div>
		</section>

		<!-- B2B SaaS Pricing Section -->
		<section id="pricing" class="py-20 border-t border-slate-800 relative">
			<div class="max-w-7xl mx-auto px-6">
				<div class="text-center max-w-3xl mx-auto">
					<h2 class="text-xs font-bold uppercase tracking-wider text-indigo-400">Transparent B2B Pricing</h2>
					<p class="mt-2 text-3xl sm:text-4xl font-extrabold text-white">Predictable Plans for Companies</p>
					<p class="mt-4 text-slate-400 text-base">
						The employer or HR lead pays the monthly plan. All employees get free self-service access on mobile & web.
					</p>

					<!-- Annual / Monthly Toggle -->
					<div class="mt-8 inline-flex items-center bg-slate-950 p-1.5 rounded-xl border border-slate-800 text-xs">
						<button
							@click="isAnnual = false"
							:class="!isAnnual ? 'bg-indigo-600 text-white font-bold' : 'text-slate-400 hover:text-white'"
							class="px-4 py-2 rounded-lg transition"
						>
							Monthly Billing
						</button>
						<button
							@click="isAnnual = true"
							:class="isAnnual ? 'bg-indigo-600 text-white font-bold' : 'text-slate-400 hover:text-white'"
							class="px-4 py-2 rounded-lg transition flex items-center space-x-1"
						>
							<span>Annual Billing</span>
							<span class="px-1.5 py-0.5 rounded-full bg-emerald-500/20 text-emerald-400 text-[10px] font-bold">Save 20%</span>
						</button>
					</div>
				</div>

				<!-- Pricing Cards Grid -->
				<div class="mt-16 grid grid-cols-1 lg:grid-cols-3 gap-8 items-stretch">
					<!-- 1. Starter Tier -->
					<div class="bg-slate-900 rounded-2xl border border-slate-800 p-8 flex flex-col justify-between">
						<div>
							<div class="flex justify-between items-center">
								<h3 class="text-lg font-bold text-white">Starter</h3>
								<span class="text-xs font-medium text-slate-400">Early Startups</span>
							</div>
							<div class="mt-4 flex items-baseline">
								<span class="text-4xl font-extrabold text-white">${{ isAnnual ? 23 : 29 }}</span>
								<span class="ml-2 text-sm text-slate-400">/ month</span>
							</div>
							<p class="mt-3 text-xs text-slate-400">Ideal for small teams getting started with structured HR.</p>

							<div class="mt-6 pt-6 border-t border-slate-800 space-y-3 text-xs text-slate-300">
								<p class="font-semibold text-white">Includes:</p>
								<div class="flex items-center space-x-2">
									<span class="text-indigo-400">✓</span>
									<span><strong>Up to 15 employees</strong></span>
								</div>
								<div class="flex items-center space-x-2">
									<span class="text-indigo-400">✓</span>
									<span>Employee Geofenced Check-in</span>
								</div>
								<div class="flex items-center space-x-2">
									<span class="text-indigo-400">✓</span>
									<span>Leave & Absence Tracking</span>
								</div>
								<div class="flex items-center space-x-2">
									<span class="text-indigo-400">✓</span>
									<span>Basic Shift Scheduling</span>
								</div>
								<div class="flex items-center space-x-2">
									<span class="text-indigo-400">✓</span>
									<span>Employee Mobile PWA</span>
								</div>
								<div class="flex items-center space-x-2">
									<span class="text-indigo-400">✓</span>
									<span>Standard Email Support</span>
								</div>
							</div>
						</div>

						<button
							@click="openModal('Starter')"
							class="mt-8 w-full py-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs border border-slate-700 transition"
						>
							Start with Starter
						</button>
					</div>

					<!-- 2. Growth Tier (Most Popular) -->
					<div class="bg-gradient-to-b from-slate-800 to-slate-900 rounded-2xl border-2 border-indigo-500 shadow-2xl shadow-indigo-500/10 p-8 flex flex-col justify-between relative transform lg:-translate-y-2">
						<div class="absolute -top-3.5 left-1/2 -translate-x-1/2 px-4 py-1 rounded-full bg-gradient-to-r from-violet-600 to-indigo-600 text-white text-[11px] font-bold tracking-wider uppercase shadow-md">
							Most Popular
						</div>

						<div>
							<div class="flex justify-between items-center mt-2">
								<h3 class="text-lg font-bold text-white">Growth</h3>
								<span class="text-xs font-semibold text-indigo-400">Scaling Teams</span>
							</div>
							<div class="mt-4 flex items-baseline">
								<span class="text-4xl font-extrabold text-white">${{ isAnnual ? 63 : 79 }}</span>
								<span class="ml-2 text-sm text-slate-400">/ month</span>
							</div>
							<p class="mt-3 text-xs text-slate-300">Complete workforce automation, payroll, and roster management.</p>

							<div class="mt-6 pt-6 border-t border-slate-700 space-y-3 text-xs text-slate-300">
								<p class="font-semibold text-white">Everything in Starter, plus:</p>
								<div class="flex items-center space-x-2">
									<span class="text-emerald-400">✓</span>
									<span><strong>Up to 50 employees</strong></span>
								</div>
								<div class="flex items-center space-x-2">
									<span class="text-emerald-400">✓</span>
									<span><strong>Automated Payroll & Salary Slips</strong></span>
								</div>
								<div class="flex items-center space-x-2">
									<span class="text-emerald-400">✓</span>
									<span>Expense Claims & Manager Approvals</span>
								</div>
								<div class="flex items-center space-x-2">
									<span class="text-emerald-400">✓</span>
									<span>Advanced Shift Rostering & Swaps</span>
								</div>
								<div class="flex items-center space-x-2">
									<span class="text-emerald-400">✓</span>
									<span>HR Desk Analytics & Reports</span>
								</div>
								<div class="flex items-center space-x-2">
									<span class="text-emerald-400">✓</span>
									<span>Priority 24/7 Slack & Email Support</span>
								</div>
							</div>
						</div>

						<button
							@click="openModal('Growth')"
							class="mt-8 w-full py-3.5 rounded-xl bg-gradient-to-r from-violet-600 via-indigo-600 to-cyan-600 hover:opacity-95 text-white font-bold text-xs shadow-lg shadow-indigo-600/30 transition transform hover:-translate-y-0.5"
						>
							Start 14-Day Free Trial
						</button>
					</div>

					<!-- 3. Enterprise Tier -->
					<div class="bg-slate-900 rounded-2xl border border-slate-800 p-8 flex flex-col justify-between">
						<div>
							<div class="flex justify-between items-center">
								<h3 class="text-lg font-bold text-white">Enterprise</h3>
								<span class="text-xs font-medium text-slate-400">High Volume</span>
							</div>
							<div class="mt-4 flex items-baseline">
								<span class="text-4xl font-extrabold text-white">${{ isAnnual ? 159 : 199 }}</span>
								<span class="ml-2 text-sm text-slate-400">/ month</span>
							</div>
							<p class="mt-3 text-xs text-slate-400">Unrestricted scale, compliance controls, and custom integrations.</p>

							<div class="mt-6 pt-6 border-t border-slate-800 space-y-3 text-xs text-slate-300">
								<p class="font-semibold text-white">Everything in Growth, plus:</p>
								<div class="flex items-center space-x-2">
									<span class="text-cyan-400">✓</span>
									<span><strong>Unlimited Employees & Seats</strong></span>
								</div>
								<div class="flex items-center space-x-2">
									<span class="text-cyan-400">✓</span>
									<span>Multi-Branch & Custom Policies</span>
								</div>
								<div class="flex items-center space-x-2">
									<span class="text-cyan-400">✓</span>
									<span>Custom Doctype Fields & Workflows</span>
								</div>
								<div class="flex items-center space-x-2">
									<span class="text-cyan-400">✓</span>
									<span>99.99% Uptime SLA Guarantee</span>
								</div>
								<div class="flex items-center space-x-2">
									<span class="text-cyan-400">✓</span>
									<span>Dedicated Enterprise Account Manager</span>
								</div>
							</div>
						</div>

						<button
							@click="openModal('Enterprise')"
							class="mt-8 w-full py-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs border border-slate-700 transition"
						>
							Contact Enterprise
						</button>
					</div>
				</div>
			</div>
		</section>

		<!-- System Architecture Overview -->
		<section id="architecture" class="py-20 bg-slate-950/60 border-t border-slate-800">
			<div class="max-w-7xl mx-auto px-6">
				<div class="text-center max-w-3xl mx-auto mb-16">
					<h2 class="text-xs font-bold uppercase tracking-wider text-indigo-400">B2B SaaS Engine</h2>
					<p class="mt-2 text-3xl sm:text-4xl font-extrabold text-white">How Eliza Multi-Tenancy Works</p>
					<p class="mt-4 text-slate-400 text-base">
						A modern 3-tier architecture ensuring complete company isolation, sub-second responses, and effortless employee onboarding.
					</p>
				</div>

				<div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-xs">
					<div class="bg-slate-900 p-6 rounded-xl border border-slate-800 space-y-3">
						<div class="text-indigo-400 font-bold uppercase text-[11px] tracking-wider">Tier 1: Cloud Database</div>
						<h4 class="text-base font-bold text-white">Neon PostgreSQL</h4>
						<p class="text-slate-400 leading-relaxed">
							Every company is partitioned by <code class="text-indigo-300">tenant_id</code>. All tables (employees, attendances, payroll, shifts) maintain strict foreign-key tenant constraints.
						</p>
						<span class="inline-block px-2.5 py-1 rounded bg-emerald-500/10 text-emerald-400 text-[10px] font-bold">
							AWS us-east-2 • Online
						</span>
					</div>

					<div class="bg-slate-900 p-6 rounded-xl border border-slate-800 space-y-3">
						<div class="text-violet-400 font-bold uppercase text-[11px] tracking-wider">Tier 2: Backend API Engine</div>
						<h4 class="text-base font-bold text-white">Multi-Tenant HTTP Core</h4>
						<p class="text-slate-400 leading-relaxed">
							Dynamic session extraction from cookies and headers automatically scopes all requests. Enforces seat quotas per subscription tier during employee invitations.
						</p>
						<span class="inline-block px-2.5 py-1 rounded bg-indigo-500/10 text-indigo-400 text-[10px] font-bold">
							Port 8000 • Autonomous Server
						</span>
					</div>

					<div class="bg-slate-900 p-6 rounded-xl border border-slate-800 space-y-3">
						<div class="text-cyan-400 font-bold uppercase text-[11px] tracking-wider">Tier 3: Dual Frontend</div>
						<h4 class="text-base font-bold text-white">Desktop Suite & Mobile PWA</h4>
						<p class="text-slate-400 leading-relaxed">
							HR leaders operate through the Vue 3 Roster & Setup Desktop Suite, while staff use the responsive Mobile PWA for geofenced check-in and leaves.
						</p>
						<span class="inline-block px-2.5 py-1 rounded bg-cyan-500/10 text-cyan-400 text-[10px] font-bold">
							Desktop 8081 & Mobile 8080
						</span>
					</div>
				</div>
			</div>
		</section>

		<!-- Frequently Asked Questions -->
		<section id="faq" class="py-20 border-t border-slate-800 max-w-4xl mx-auto px-6 w-full">
			<div class="text-center mb-12">
				<h2 class="text-xs font-bold uppercase tracking-wider text-indigo-400">Answers to Your Questions</h2>
				<p class="mt-2 text-3xl font-extrabold text-white">Frequently Asked Questions</p>
			</div>

			<div class="space-y-4">
				<div
					v-for="(faq, idx) in faqs"
					:key="idx"
					class="bg-slate-900 rounded-xl border border-slate-800 overflow-hidden"
				>
					<button
						@click="faq.open = !faq.open"
						class="w-full p-5 text-left flex justify-between items-center text-sm font-bold text-slate-200 hover:text-white transition"
					>
						<span>{{ faq.question }}</span>
						<svg
							:class="faq.open ? 'rotate-180 text-indigo-400' : 'text-slate-500'"
							class="w-4 h-4 transform transition-transform"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
						</svg>
					</button>
					<div v-show="faq.open" class="px-5 pb-5 text-xs text-slate-400 leading-relaxed border-t border-slate-800/60 pt-3">
						{{ faq.answer }}
					</div>
				</div>
			</div>
		</section>

		<!-- Bottom Call-to-Action -->
		<section class="py-20 bg-gradient-to-b from-slate-900 to-slate-950 border-t border-slate-800 text-center relative overflow-hidden">
			<div class="max-w-4xl mx-auto px-6 relative z-10">
				<h2 class="text-3xl sm:text-5xl font-extrabold text-white">
					Ready to Upgrade Your Company's HR?
				</h2>
				<p class="mt-4 text-slate-400 text-base max-w-2xl mx-auto">
					Join ambitious companies who run on Eliza. Get started with a 14-day free trial — no credit card required.
				</p>
				<div class="mt-8 flex flex-col sm:flex-row items-center justify-center gap-4">
					<button
						@click="openModal('Growth')"
						class="px-8 py-3.5 text-sm font-bold rounded-xl text-white bg-gradient-to-r from-violet-600 via-indigo-600 to-cyan-600 hover:opacity-95 shadow-xl shadow-indigo-600/30 transition transform hover:-translate-y-0.5"
					>
						Start Free Company Trial
					</button>
					<router-link
						to="/desk/hr-setup"
						class="px-6 py-3.5 text-sm font-semibold rounded-xl text-slate-300 bg-slate-800 hover:bg-slate-700 border border-slate-700 transition"
					>
						View Demo Workspace
					</router-link>
				</div>
			</div>
		</section>

		<!-- Footer -->
		<footer class="bg-slate-950 border-t border-slate-800/80 py-12 text-xs text-slate-500">
			<div class="max-w-7xl mx-auto px-6 flex flex-col sm:flex-row items-center justify-between gap-6">
				<div class="flex items-center space-x-3">
					<div class="h-7 w-7 rounded-lg bg-indigo-600 flex items-center justify-center font-black text-white text-sm">
						E
					</div>
					<span class="text-slate-300 font-bold text-sm">Eliza HR</span>
					<span>•</span>
					<span>© 2026 Eliza Inc. All rights reserved.</span>
				</div>

				<div class="flex items-center space-x-6 text-slate-400">
					<router-link to="/desk/hr-setup" class="hover:text-white transition">HR Setup</router-link>
					<router-link to="/roster" class="hover:text-white transition">Roster View</router-link>
					<a href="http://127.0.0.1:8080" target="_blank" class="hover:text-white transition">Employee PWA</a>
					<span class="flex items-center space-x-1.5 text-emerald-400">
						<span class="h-2 w-2 rounded-full bg-emerald-400 animate-pulse"></span>
						<span>All Systems Operational</span>
					</span>
				</div>
			</div>
		</footer>

		<!-- Company Registration / Onboarding Modal -->
		<div
			v-if="showModal"
			class="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/80 backdrop-blur-md transition-opacity"
		>
			<div class="bg-slate-900 border border-slate-700 rounded-2xl max-w-lg w-full p-6 sm:p-8 shadow-2xl relative">
				<!-- Close Button -->
				<button
					@click="showModal = false"
					class="absolute top-5 right-5 text-slate-400 hover:text-white p-1 rounded-lg hover:bg-slate-800 transition"
				>
					<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
					</svg>
				</button>

				<!-- Modal Header -->
				<div class="text-left">
					<div class="h-10 w-10 rounded-xl bg-gradient-to-tr from-violet-600 to-indigo-600 flex items-center justify-center text-white font-black text-lg mb-4">
						E
					</div>
					<h3 class="text-2xl font-extrabold text-white">Register Your Company on Eliza</h3>
					<p class="text-xs text-slate-400 mt-1">
						You are registering as the <strong class="text-indigo-300">Company Lead / HR Admin</strong>. All employees you invite will access self-service features for free.
					</p>
				</div>

				<!-- Success Banner -->
				<div v-if="successMessage" class="mt-4 p-4 rounded-xl bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-xs flex items-center space-x-3">
					<svg class="w-5 h-5 flex-shrink-0 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
					</svg>
					<div>
						<p class="font-bold text-white">{{ successMessage }}</p>
						<p class="text-[11px] text-emerald-400 mt-0.5">Redirecting to your HR Setup Workspace in {{ redirectCountdown }}s...</p>
					</div>
				</div>

				<!-- Error Banner -->
				<div v-if="errorMessage" class="mt-4 p-3 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-300 text-xs">
					{{ errorMessage }}
				</div>

				<!-- Form Inputs -->
				<form v-if="!successMessage" @submit.prevent="submitRegistration" class="mt-6 space-y-4 text-xs">
					<div>
						<label class="block font-semibold text-slate-300 mb-1">Company / Organization Name</label>
						<input
							v-model="form.company_name"
							type="text"
							required
							placeholder="e.g. Acme Technologies Inc."
							class="w-full px-3.5 py-2.5 rounded-xl bg-slate-800 border border-slate-700 text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition"
						/>
					</div>

					<div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
						<div>
							<label class="block font-semibold text-slate-300 mb-1">Lead Full Name</label>
							<input
								v-model="form.admin_name"
								type="text"
								required
								placeholder="e.g. Sarah Jenkins"
								class="w-full px-3.5 py-2.5 rounded-xl bg-slate-800 border border-slate-700 text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition"
							/>
						</div>
						<div>
							<label class="block font-semibold text-slate-300 mb-1">Work Email</label>
							<input
								v-model="form.admin_email"
								type="email"
								required
								placeholder="sarah@acme.com"
								class="w-full px-3.5 py-2.5 rounded-xl bg-slate-800 border border-slate-700 text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition"
							/>
						</div>
					</div>

					<div>
						<label class="block font-semibold text-slate-300 mb-1">Account Password</label>
						<input
							v-model="form.password"
							type="password"
							required
							placeholder="••••••••••••"
							class="w-full px-3.5 py-2.5 rounded-xl bg-slate-800 border border-slate-700 text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition"
						/>
					</div>

					<div>
						<label class="block font-semibold text-slate-300 mb-1">Selected Plan Tier</label>
						<div class="grid grid-cols-3 gap-2">
							<button
								type="button"
								v-for="plan in ['Starter', 'Growth', 'Enterprise']"
								:key="plan"
								@click="form.plan_tier = plan"
								:class="form.plan_tier === plan ? 'bg-indigo-600 text-white border-indigo-500 font-bold' : 'bg-slate-800 text-slate-400 border-slate-700 hover:text-white'"
								class="py-2 rounded-lg border text-xs transition"
							>
								{{ plan }}
							</button>
						</div>
					</div>

					<div class="pt-2">
						<button
							type="submit"
							:disabled="isSubmitting"
							class="w-full py-3 rounded-xl bg-gradient-to-r from-violet-600 via-indigo-600 to-cyan-600 hover:opacity-95 text-white font-bold text-xs shadow-lg shadow-indigo-600/30 transition flex items-center justify-center space-x-2 disabled:opacity-50"
						>
							<svg v-if="isSubmitting" class="animate-spin h-4 w-4 text-white" fill="none" viewBox="0 0 24 24">
								<circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
								<path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
							</svg>
							<span>{{ isSubmitting ? 'Creating Workspace...' : 'Create Company Workspace' }}</span>
						</button>
					</div>

					<p class="text-[10px] text-center text-slate-500">
						By registering, you agree to Eliza's Terms of Service and Privacy Policy. Includes a 14-day full feature trial.
					</p>
				</form>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
import { ref, computed } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

// State
const activePreviewTab = ref("shifts");
const isAnnual = ref(false);
const teamSize = ref(25);
const showModal = ref(false);
const isSubmitting = ref(false);
const errorMessage = ref("");
const successMessage = ref("");
const redirectCountdown = ref(3);

const form = ref({
	company_name: "",
	admin_name: "",
	admin_email: "",
	password: "",
	plan_tier: "Growth",
});

const previewTabs = [
	{ id: "shifts", name: "Shift Rostering" },
	{ id: "employees", name: "Employee Directory" },
	{ id: "attendance", name: "Live Check-in" },
	{ id: "payroll", name: "Automated Payroll" },
];

const faqs = ref([
	{
		question: "Who pays the monthly fee for Eliza?",
		answer: "The company or HR lead is the primary subscriber who pays a flat monthly fee based on your seat tier. All invited employees access their mobile and web self-service tools completely free.",
		open: true,
	},
	{
		question: "Can employees clock in from their mobile phones?",
		answer: "Yes! Eliza includes an installable Mobile PWA optimized for iOS and Android. Employees can clock in/out with geofencing, submit leave requests, view upcoming shifts, and download payslips.",
		open: false,
	},
	{
		question: "How does multi-tenant data separation work?",
		answer: "Every organization has a dedicated tenant_id in our Neon PostgreSQL database. All records—from salary slips to shift rosters—are partition-scoped so there is zero data crossover between companies.",
		open: false,
	},
	{
		question: "Can I upgrade or downgrade plans anytime?",
		answer: "Yes, you can upgrade, downgrade, or cancel your subscription at any time without penalty. When you upgrade, your seat limit is expanded immediately.",
		open: false,
	},
]);

// Calculator Computeds
const calculatedPlan = computed(() => {
	if (teamSize.value <= 15) {
		return { name: "Starter", price: isAnnual.value ? 23 : 29 };
	} else if (teamSize.value <= 50) {
		return { name: "Growth", price: isAnnual.value ? 63 : 79 };
	} else {
		return { name: "Enterprise", price: isAnnual.value ? 159 : 199 };
	}
});

const calculatedHoursSaved = computed(() => {
	return Math.round(teamSize.value * 1.4);
});

// Actions
function scrollToTop() {
	window.scrollTo({ top: 0, behavior: "smooth" });
}

function openModal(plan: string) {
	form.value.plan_tier = plan;
	errorMessage.value = "";
	successMessage.value = "";
	showModal.value = true;
}

async function submitRegistration() {
	isSubmitting.value = true;
	errorMessage.value = "";
	successMessage.value = "";

	try {
		const response = await fetch("/api/method/saas.register_company", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
				"X-Tenant-Id": "NEW",
			},
			body: JSON.stringify(form.value),
		});

		const result = await response.json();

		if (response.ok && result.message && result.message.status === "success") {
			successMessage.value = `Welcome to Eliza! Registered ${form.value.company_name} on the ${form.value.plan_tier} Plan.`;
			
			// Countdown timer and redirect
			let count = 3;
			redirectCountdown.value = count;
			const interval = setInterval(() => {
				count -= 1;
				redirectCountdown.value = count;
				if (count <= 0) {
					clearInterval(interval);
					showModal.value = false;
					router.push("/desk/hr-setup");
				}
			}, 1000);
		} else {
			errorMessage.value = result._error_message || result.exc || "Failed to register company. Please try again.";
		}
	} catch (err: any) {
		errorMessage.value = err.message || "Network error reaching Eliza backend server.";
	} finally {
		isSubmitting.value = false;
	}
}
</script>
