


<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>HPJA/HFSPlus_sStructure.py at master · HFSPlusJournalAnalyzer/HPJA</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="HFSPlusJournalAnalyzer/HPJA" name="twitter:title" /><meta content="HPJA - HFSPlusJournalAnalyzer" name="twitter:description" /><meta content="https://avatars1.githubusercontent.com/u/10630908?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars1.githubusercontent.com/u/10630908?v=3&amp;s=400" property="og:image" /><meta content="HFSPlusJournalAnalyzer/HPJA" property="og:title" /><meta content="https://github.com/HFSPlusJournalAnalyzer/HPJA" property="og:url" /><meta content="HPJA - HFSPlusJournalAnalyzer" property="og:description" />
      <meta name="browser-stats-url" content="/_stats">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    <link rel="xhr-socket" href="/_sockets">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="7D83BD3D:0FF6:1174584:54DD7DD4" name="octolytics-dimension-request_id" /><meta content="9063308" name="octolytics-actor-id" /><meta content="biscuit03" name="octolytics-actor-login" /><meta content="bda193a693410a86db1459d2239b6fcc5c2f36daccee16c1496ebd507be5d4f4" name="octolytics-actor-hash" />
    
    <meta content="Rails, view, blob#show" name="analytics-event" />

    
    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="U25rCbptH+X7PBtcCf2MS3HBwZIbThWd9YeBZpdmlV5957U6LbMhwpWmpNKtfi9jXGWxtko9kw77jYc+0fhj0Q==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-7f7a8d43d99dce26334cc1cb3b327f57a9309f9d6f215d6f3dff77d5e0c593a3.css" media="all" rel="stylesheet" />
    <link href="https://assets-cdn.github.com/assets/github2-a8f2a7df6fdc952a46bc2ca532f6648544a4e0a803dba39a318d244baa77bbd5.css" media="all" rel="stylesheet" />
    
    


    <meta http-equiv="x-pjax-version" content="b3941243dd1d2edbd89ff1829245b524">

      
  <meta name="description" content="HPJA - HFSPlusJournalAnalyzer">
  <meta name="go-import" content="github.com/HFSPlusJournalAnalyzer/HPJA git https://github.com/HFSPlusJournalAnalyzer/HPJA.git">

  <meta content="10630908" name="octolytics-dimension-user_id" /><meta content="HFSPlusJournalAnalyzer" name="octolytics-dimension-user_login" /><meta content="29588629" name="octolytics-dimension-repository_id" /><meta content="HFSPlusJournalAnalyzer/HPJA" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="29588629" name="octolytics-dimension-repository_network_root_id" /><meta content="HFSPlusJournalAnalyzer/HPJA" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/HFSPlusJournalAnalyzer/HPJA/commits/master.atom" rel="alternate" title="Recent Commits to HPJA:master" type="application/atom+xml">

  </head>


  <body class="logged_in  env-production windows vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" ga-data-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <form accept-charset="UTF-8" action="/HFSPlusJournalAnalyzer/HPJA/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/HFSPlusJournalAnalyzer/HPJA/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <input type="text"
    class="js-site-search-field is-clearable"
    data-hotkey="s"
    name="q"
    placeholder="Search"
    data-global-scope-placeholder="Search GitHub"
    data-repo-scope-placeholder="Search"
    tabindex="1"
    autocapitalize="off">
  <div class="scope-badge">This repository</div>
</form>
      </div>
      <ul class="header-nav left" role="navigation">
        <li class="header-nav-item explore">
          <a class="header-nav-link" href="/explore" data-ga-click="Header, go to explore, text:explore">Explore</a>
        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/blog" data-ga-click="Header, go to blog, text:blog">Blog</a>
          </li>
        <li class="header-nav-item">
          <a class="header-nav-link" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
        </li>
      </ul>

    
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name" href="/biscuit03" data-ga-click="Header, go to profile, text:username">
      <img alt="biscuit03" class="avatar" data-user="9063308" height="20" src="https://avatars1.githubusercontent.com/u/9063308?v=3&amp;s=40" width="20" />
      <span class="css-truncate">
        <span class="css-truncate-target">biscuit03</span>
      </span>
    </a>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link js-menu-target tooltipped tooltipped-s" href="#" aria-label="Create new..." data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      
<ul class="dropdown-menu">
  <li>
    <a href="/new" data-ga-click="Header, create new repository, icon:repo"><span class="octicon octicon-repo"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new" data-ga-click="Header, create new organization, icon:organization"><span class="octicon octicon-organization"></span> New organization</a>
  </li>


    <li class="dropdown-divider"></li>
    <li class="dropdown-header">
      <span title="HFSPlusJournalAnalyzer/HPJA">This repository</span>
    </li>
      <li>
        <a href="/HFSPlusJournalAnalyzer/HPJA/issues/new" data-ga-click="Header, create new issue, icon:issue"><span class="octicon octicon-issue-opened"></span> New issue</a>
      </li>
      <li>
        <a href="/HFSPlusJournalAnalyzer/HPJA/settings/collaboration" data-ga-click="Header, create new collaborator, icon:person"><span class="octicon octicon-person"></span> New collaborator</a>
      </li>
</ul>

    </div>
  </li>

  <li class="header-nav-item">
        <a href="/notifications" aria-label="You have no unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:read" data-hotkey="g n">
        <span class="mail-status all-read"></span>
        <span class="octicon octicon-inbox"></span>
</a>
  </li>

  <li class="header-nav-item">
    <a class="header-nav-link tooltipped tooltipped-s" href="/settings/profile" id="account_settings" aria-label="Settings" data-ga-click="Header, go to settings, icon:settings">
      <span class="octicon octicon-gear"></span>
    </a>
  </li>

  <li class="header-nav-item">
    <form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="1TXmq5jgir7iV5czUHF8vu1VkKLcJGYjwvXt1b3X9K3d3bZbwbP5TmgE0yUS7vKQ+pw5bYYhXLoyp+Sl4NErKQ==" /></div>
      <button class="header-nav-link sign-out-button tooltipped tooltipped-s" aria-label="Sign out" data-ga-click="Header, sign out, icon:logout">
        <span class="octicon octicon-sign-out"></span>
      </button>
</form>  </li>

</ul>


    
  </div>
</div>

      

        


      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">

  <li>
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="xDKFsj9Qg0Nwq+UeqK2CNqzBb+YTkDbw9aMUKGrE4dlh6lO2krXgIsGHS63SmR/xb816CUWaQYSPVPH+APPEbw==" /></div>    <input id="repository_id" name="repository_id" type="hidden" value="29588629" />

      <div class="select-menu js-menu-container js-select-menu">
        <a class="social-count js-social-count" href="/HFSPlusJournalAnalyzer/HPJA/watchers">
          3
        </a>
        <a href="/HFSPlusJournalAnalyzer/HPJA/subscription"
          class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0" aria-haspopup="true">
          <span class="js-select-button">
            <span class="octicon octicon-eye"></span>
            Unwatch
          </span>
        </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header">
              <span class="select-menu-title">Notifications</span>
              <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
            </div>

            <div class="select-menu-list js-navigation-container" role="menu">

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_included" name="do" type="radio" value="included" />
                  <span class="select-menu-item-heading">Not watching</span>
                  <span class="description">Be notified when participating or @mentioned.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Watch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                  <span class="select-menu-item-heading">Watching</span>
                  <span class="description">Be notified of all conversations.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Unwatch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_ignore" name="do" type="radio" value="ignore" />
                  <span class="select-menu-item-heading">Ignoring</span>
                  <span class="description">Never be notified.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-mute"></span>
                    Stop ignoring
                  </span>
                </div>
              </div>

            </div>

          </div>
        </div>
      </div>
</form>

  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <form accept-charset="UTF-8" action="/HFSPlusJournalAnalyzer/HPJA/unstar" class="js-toggler-form starred js-unstar-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="JpZVnhuoWCMiRrKbxpghcTpJhrszbsDlg+jU1v7OwOeD6nwRYTLldLL0v8O2SIaqPXp46QutPxJ/m3YNvzWlFA==" /></div>
      <button
        class="minibutton with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar HFSPlusJournalAnalyzer/HPJA">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/HFSPlusJournalAnalyzer/HPJA/stargazers">
          0
        </a>
</form>
    <form accept-charset="UTF-8" action="/HFSPlusJournalAnalyzer/HPJA/star" class="js-toggler-form unstarred js-star-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="bwwWxNOrtv9WJecbiLjcmTivLOttq/8D1GcRH39hSmoaftO97dJpCalBd6ks6ICuJL6ZTJoiGP0+KnYbS45z3w==" /></div>
      <button
        class="minibutton with-count js-toggler-target"
        aria-label="Star this repository" title="Star HFSPlusJournalAnalyzer/HPJA">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/HFSPlusJournalAnalyzer/HPJA/stargazers">
          0
        </a>
</form>  </div>

  </li>

        <li>
          <a href="/HFSPlusJournalAnalyzer/HPJA/fork" class="minibutton with-count js-toggler-target tooltipped-n" title="Fork your own copy of HFSPlusJournalAnalyzer/HPJA to your account" aria-label="Fork your own copy of HFSPlusJournalAnalyzer/HPJA to your account" rel="facebox nofollow">
            <span class="octicon octicon-repo-forked"></span>
            Fork
          </a>
          <a href="/HFSPlusJournalAnalyzer/HPJA/network" class="social-count">0</a>
        </li>

</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/HFSPlusJournalAnalyzer" class="url fn" itemprop="url" rel="author"><span itemprop="title">HFSPlusJournalAnalyzer</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/HFSPlusJournalAnalyzer/HPJA" class="js-current-repository" data-pjax="#js-repo-pjax-container">HPJA</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/HFSPlusJournalAnalyzer/HPJA/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/HFSPlusJournalAnalyzer/HPJA" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /HFSPlusJournalAnalyzer/HPJA">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/HFSPlusJournalAnalyzer/HPJA/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /HFSPlusJournalAnalyzer/HPJA/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
      <a href="/HFSPlusJournalAnalyzer/HPJA/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /HFSPlusJournalAnalyzer/HPJA/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>


      <li class="tooltipped tooltipped-w" aria-label="Wiki">
        <a href="/HFSPlusJournalAnalyzer/HPJA/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g w" data-selected-links="repo_wiki /HFSPlusJournalAnalyzer/HPJA/wiki">
          <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>
  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/HFSPlusJournalAnalyzer/HPJA/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /HFSPlusJournalAnalyzer/HPJA/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/HFSPlusJournalAnalyzer/HPJA/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /HFSPlusJournalAnalyzer/HPJA/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>
  </ul>


    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">
      <li class="tooltipped tooltipped-w" aria-label="Settings">
        <a href="/HFSPlusJournalAnalyzer/HPJA/settings" aria-label="Settings" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_settings /HFSPlusJournalAnalyzer/HPJA/settings">
          <span class="octicon octicon-tools"></span> <span class="full-word">Settings</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>
    </ul>
</nav>

              <div class="only-with-full-nav">
                  
<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/HFSPlusJournalAnalyzer/HPJA.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=clone">
  <h3><span class="text-emphasized">SSH</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="git@github.com:HFSPlusJournalAnalyzer/HPJA.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/HFSPlusJournalAnalyzer/HPJA" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



<p class="clone-options">You can clone with
  <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>, <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>, or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>


  <a href="github-windows://openRepo/https://github.com/HFSPlusJournalAnalyzer/HPJA" class="minibutton sidebar-button" title="Save HFSPlusJournalAnalyzer/HPJA to your computer and use it in GitHub Desktop." aria-label="Save HFSPlusJournalAnalyzer/HPJA to your computer and use it in GitHub Desktop.">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>

                <a href="/HFSPlusJournalAnalyzer/HPJA/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download the contents of HFSPlusJournalAnalyzer/HPJA as a zip file"
                   title="Download the contents of HFSPlusJournalAnalyzer/HPJA as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          

<a href="/HFSPlusJournalAnalyzer/HPJA/blob/f229ec350ce4175a00e4497c68bbc2d404cfc7e7/Working/HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217/HFSPlus_sStructure.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:734d8eba51204bd5d67999695f1b9fbf -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu js-menu-container js-select-menu left">
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Find or create a branch…" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/HFSPlusJournalAnalyzer/HPJA/blob/master/Working/HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217/HFSPlus_sStructure.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text css-truncate-target"
                 title="master">master</a>
            </div>
        </div>

          <form accept-charset="UTF-8" action="/HFSPlusJournalAnalyzer/HPJA/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="nCVhQ/dKUJKAY0vziKclniEXUDTtOlVE8V9y5acJWPrpY67cWp5dH123LtJ37kfcoYO0CDXWcOuDHRHWe7BqEQ==" /></div>
            <span class="octicon octicon-git-branch select-menu-item-icon"></span>
            <div class="select-menu-item-text">
              <span class="select-menu-item-heading">Create branch: <span class="js-new-item-name"></span></span>
              <span class="description">from ‘master’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master">
            <input type="hidden" name="path" id="path" value="Working/HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217/HFSPlus_sStructure.py">
</form>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="button-group right">
    <a href="/HFSPlusJournalAnalyzer/HPJA/find/master"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>

  <div class="breadcrumb js-zeroclipboard-target">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/HFSPlusJournalAnalyzer/HPJA" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">HPJA</span></a></span></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/HFSPlusJournalAnalyzer/HPJA/tree/master/Working" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">Working</span></a></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/HFSPlusJournalAnalyzer/HPJA/tree/master/Working/HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217</span></a></span><span class="separator">/</span><strong class="final-path">HFSPlus_sStructure.py</strong>
  </div>
</div>

<include-fragment class="commit commit-loader file-history-tease" src="/HFSPlusJournalAnalyzer/HPJA/contributors/master/Working/HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217/HFSPlus_sStructure.py">
  <div class="file-history-tease-header">
    Fetching contributors&hellip;
  </div>

  <div class="participation">
    <p class="loader-loading"><img alt="" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-EAF2F5-0bdc57d34b85c4a4de9d0d1db10cd70e8a95f33ff4f46c5a8c48b4bf4e5a9abe.gif" width="16" /></p>
    <p class="loader-error">Cannot retrieve contributors at this time</p>
  </div>
</include-fragment>
<div class="file-box">
  <div class="file">
    <div class="meta clearfix">
      <div class="info file-name">
          <span>150 lines (112 sloc)</span>
          <span class="meta-divider"></span>
        <span>6.48 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
          <a href="/HFSPlusJournalAnalyzer/HPJA/raw/master/Working/HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217/HFSPlus_sStructure.py" class="minibutton " id="raw-url">Raw</a>
            <a href="/HFSPlusJournalAnalyzer/HPJA/blame/master/Working/HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217/HFSPlus_sStructure.py" class="minibutton js-update-url-with-hash">Blame</a>
          <a href="/HFSPlusJournalAnalyzer/HPJA/commits/master/Working/HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217/HFSPlus_sStructure.py" class="minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->

          <a class="octicon-button tooltipped tooltipped-nw"
             href="github-windows://openRepo/https://github.com/HFSPlusJournalAnalyzer/HPJA?branch=master&amp;filepath=Working%2FHFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217%2FHFSPlus_sStructure.py" aria-label="Open this file in GitHub for Windows">
              <span class="octicon octicon-device-desktop"></span>
          </a>

              <a class="octicon-button js-update-url-with-hash"
                 href="/HFSPlusJournalAnalyzer/HPJA/edit/master/Working/HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217/HFSPlus_sStructure.py"
                 aria-label="Edit this file"
                 data-method="post" rel="nofollow" data-hotkey="e"><span class="octicon octicon-pencil"></span></a>

            <a class="octicon-button danger"
               href="/HFSPlusJournalAnalyzer/HPJA/delete/master/Working/HFSPlusJournalAnalyzer_ver2.0_2015-02-13-1217/HFSPlus_sStructure.py"
               aria-label="Delete this file"
               data-method="post" data-test-id="delete-blob-file" rel="nofollow">
          <span class="octicon octicon-trashcan"></span>
        </a>
      </div><!-- /.actions -->
    </div>
    

  <div class="blob-wrapper data type-python">
      <table class="highlight tab-size-8 js-file-line-container">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code js-file-line"><span class="pl-k">from</span> collections <span class="pl-k">import</span> namedtuple</td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code js-file-line">JournalHeader <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&quot;</span>JournalHeader<span class="pl-pds">&quot;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>magic<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>endian<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>start<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>end<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>size<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>blhdr_size<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>checksum<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>jhdr_size<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code js-file-line"><span class="pl-c"># endian contains &#39;&gt;&#39; or &#39;&lt;&#39; (instead of 0x12345678; the original value) </span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code js-file-line">BlockListHeader <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&quot;</span>BlockListHeader<span class="pl-pds">&quot;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>max_blocks<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>num_blocks<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>bytes_used<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>checksum<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>pad<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>binfo0<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code js-file-line">BlockInfo <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&quot;</span>BlockInfo<span class="pl-pds">&quot;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>bnum<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>bsize<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>next<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code js-file-line">NodeDescriptor <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&quot;</span>NodeDescriptor<span class="pl-pds">&quot;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>fLink<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>bLink<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>kind<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>height<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>numRecords<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>reserved<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code js-file-line">BTHeaderRec <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&quot;</span>BTHeaderRec<span class="pl-pds">&quot;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>treeDepth<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>rootNode<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code js-file-line">                                        <span class="pl-s1"><span class="pl-pds">&#39;</span>leafRecords<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>firstLeafNode<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>lastLeafNode<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>nodeSize<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code js-file-line">                                        <span class="pl-s1"><span class="pl-pds">&#39;</span>maxKeyLength<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>totalNodes<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>freeNodes<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>reserved1<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code js-file-line">                                        <span class="pl-s1"><span class="pl-pds">&#39;</span>clumpSize<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>btreeType<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code js-file-line">                                        <span class="pl-s1"><span class="pl-pds">&#39;</span>keyCompareType<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>attributes<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code js-file-line">VolumeHeader <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&quot;</span>VolumeHeader<span class="pl-pds">&quot;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>signature<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>version<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>attributes<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>lastMountedVersion<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>journalInfoBlock<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code js-file-line">                                          <span class="pl-s1"><span class="pl-pds">&#39;</span>createDate<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>modifyDate<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>backupDate<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>checkedDate<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code js-file-line">                                          <span class="pl-s1"><span class="pl-pds">&#39;</span>fileCount<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>folderCount<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code js-file-line">                                          <span class="pl-s1"><span class="pl-pds">&#39;</span>blockSize<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>totalBlocks<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>freeBlocks<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>nextAllocation<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code js-file-line">                                          <span class="pl-s1"><span class="pl-pds">&#39;</span>rsrcClumpSize<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>dataClumpSize<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code js-file-line">                                          <span class="pl-s1"><span class="pl-pds">&#39;</span>nextCatalogID<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>writeCount<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code js-file-line">                                          <span class="pl-s1"><span class="pl-pds">&#39;</span>encodingsBitmap<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>finderInfo<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code js-file-line">                                          <span class="pl-s1"><span class="pl-pds">&#39;</span>allocationFile<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>extentsFile<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>catalogFile<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>attributesFile<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>startupFile<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code js-file-line"><span class="pl-s1"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code js-file-line"><span class="pl-s1"> Leaf Records  </span></td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code js-file-line"><span class="pl-s1"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code js-file-line">ExtentDescriptor <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&quot;</span>ExtentDescriptor<span class="pl-pds">&quot;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>startBlock<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>blockCount<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code js-file-line">ForkData <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&quot;</span>ForkData<span class="pl-pds">&quot;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>logicalSize<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>clumpSize<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>totalBlocks<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>extents<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code js-file-line"><span class="pl-st">class</span> <span class="pl-en">BTKey</span>(<span class="pl-e">namedtuple(<span class="pl-s1"><span class="pl-pds">&quot;</span>BTKey<span class="pl-pds">&quot;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>keyLength<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>key<span class="pl-pds">&#39;</span></span>])</span>):</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code js-file-line">    __slot__ <span class="pl-k">=</span> ()</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__len__</span></span>(<span class="pl-vpf">self</span>):</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">2</span> <span class="pl-k">+</span> <span class="pl-s3">len</span>(<span class="pl-v">self</span>.key)</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__eq__</span></span>(<span class="pl-vpf">self</span>, <span class="pl-vpf">other</span>):</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code js-file-line">        kL_Comp <span class="pl-k">=</span> (<span class="pl-v">self</span>.keyLength <span class="pl-k">==</span> other.keyLength)</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code js-file-line">        key_Comp <span class="pl-k">=</span> (<span class="pl-v">self</span>.key <span class="pl-k">==</span> other.key)</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code js-file-line">        <span class="pl-k">return</span> (kL_Comp <span class="pl-k">and</span> key_Comp)</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code js-file-line">BSDInfo <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&quot;</span>BSDInfo<span class="pl-pds">&quot;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>ownerID<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>groupID<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>adminFlags<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>ownerFlags<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>fileMode<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>special<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code js-file-line"><span class="pl-s1"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code js-file-line"><span class="pl-s1">Finder</span></td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code js-file-line"><span class="pl-s1"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code js-file-line">Point <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&#39;</span>Point<span class="pl-pds">&#39;</span></span>, [<span class="pl-s1"><span class="pl-pds">&quot;</span>v<span class="pl-pds">&quot;</span></span>, <span class="pl-s1"><span class="pl-pds">&quot;</span>h<span class="pl-pds">&quot;</span></span>])</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code js-file-line">Rect <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&#39;</span>Rect<span class="pl-pds">&#39;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>top<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>left<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>bottom<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>right<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code js-file-line">FileInfo <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&#39;</span>FileInfo<span class="pl-pds">&#39;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>fileType<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>fileCreator<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>finderFlags<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>location<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>reservedField<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code js-file-line">ExtendedFileInfo <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&quot;</span>ExtendedFileInfo<span class="pl-pds">&quot;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>reserved1<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>extendedFinderFlags<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>reserved2<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>putAwayFolderID<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code js-file-line">FolderInfo <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&#39;</span>FolderInfo<span class="pl-pds">&#39;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>windowBounds<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>finderFlags<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>location<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>reservedField<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code js-file-line">ExtendedFolderInfo <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&quot;</span>ExtendedFolderInfo<span class="pl-pds">&quot;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>scrollPosition<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>reserved1<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>extendedFinderFlags<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>reserved2<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>putAwayFolderID<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code js-file-line"><span class="pl-s1"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code js-file-line"><span class="pl-s1">Catalog Records </span></td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code js-file-line"><span class="pl-s1"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code js-file-line"><span class="pl-st">class</span> <span class="pl-en">CatalogLeafRec</span>(<span class="pl-e">namedtuple(<span class="pl-s1"><span class="pl-pds">&quot;</span>CatalogLeafRec<span class="pl-pds">&quot;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>key<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>record<span class="pl-pds">&#39;</span></span>])</span>):</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code js-file-line">    <span class="pl-sv">__slots__</span> <span class="pl-k">=</span> ()</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__len__</span></span>(<span class="pl-vpf">self</span>):</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code js-file-line">        <span class="pl-k">return</span> <span class="pl-s3">len</span>(<span class="pl-v">self</span>.key) <span class="pl-k">+</span> <span class="pl-s3">len</span>(<span class="pl-v">self</span>.record)</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__eq__</span></span>(<span class="pl-vpf">self</span>, <span class="pl-vpf">other</span>):</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code js-file-line">        keyComp <span class="pl-k">=</span> ( <span class="pl-v">self</span>.key <span class="pl-k">==</span> other.key )</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code js-file-line">        recComp <span class="pl-k">=</span> ( <span class="pl-v">self</span>.record <span class="pl-k">==</span> other.record )</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code js-file-line">        <span class="pl-k">return</span> (keyComp <span class="pl-k">and</span> recComp)</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code js-file-line">        </td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code js-file-line"><span class="pl-st">class</span> <span class="pl-en">CatalogKey</span>(<span class="pl-e">namedtuple(<span class="pl-s1"><span class="pl-pds">&quot;</span>CatalogKey<span class="pl-pds">&quot;</span></span>, [<span class="pl-s1"><span class="pl-pds">&quot;</span>parentID<span class="pl-pds">&quot;</span></span>, <span class="pl-s1"><span class="pl-pds">&quot;</span>nodeName<span class="pl-pds">&quot;</span></span>])</span>):</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code js-file-line">    <span class="pl-sv">__slots__</span> <span class="pl-k">=</span> ()</td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__len__</span></span>(<span class="pl-vpf">self</span>):</td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">4</span><span class="pl-k">+</span><span class="pl-c1">2</span><span class="pl-k">+</span><span class="pl-c1">2</span><span class="pl-k">*</span><span class="pl-v">self</span>.nodeName[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__eq__</span></span>(<span class="pl-vpf">self</span>, <span class="pl-vpf">other</span>):</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code js-file-line">        <span class="pl-k">return</span> (<span class="pl-v">self</span>.nodeName <span class="pl-k">==</span> other.nodeName)</td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__hash__</span></span>(<span class="pl-vpf">self</span>):</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code js-file-line">        <span class="pl-k">return</span> <span class="pl-s3">hash</span>(<span class="pl-v">self</span>.nodeName)</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code js-file-line">     </td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code js-file-line">sCatalogFolder <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&#39;</span>CatalogFolder<span class="pl-pds">&#39;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>recordType<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>flags<span class="pl-pds">&#39;</span></span>, </td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code js-file-line">                                             <span class="pl-s1"><span class="pl-pds">&#39;</span>valence<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>folderID<span class="pl-pds">&#39;</span></span>, </td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code js-file-line">                                             <span class="pl-s1"><span class="pl-pds">&#39;</span>createDate<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>contentModDate<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>attributeModDate<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>accessDate<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>backupDate<span class="pl-pds">&#39;</span></span>, </td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code js-file-line">                                             <span class="pl-s1"><span class="pl-pds">&#39;</span>permissions<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>userInfo<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>finderInfo<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code js-file-line">                                             <span class="pl-s1"><span class="pl-pds">&#39;</span>textEncoding<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>reserved<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code js-file-line"><span class="pl-st">class</span> <span class="pl-en">CatalogFolder</span>(<span class="pl-e">sCatalogFolder</span>):</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code js-file-line">    <span class="pl-sv">__slots__</span> <span class="pl-k">=</span> ()</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__len__</span></span>(<span class="pl-vpf">self</span>):</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">88</span></td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__eq__</span></span>(<span class="pl-vpf">self</span>, <span class="pl-vpf">other</span>):</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code js-file-line">        <span class="pl-k">return</span> ((<span class="pl-v">self</span>.recordType <span class="pl-k">==</span> other.recordType) <span class="pl-k">and</span> (<span class="pl-v">self</span>.folderID <span class="pl-k">==</span> other.folderID))</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__hash__</span></span>(<span class="pl-vpf">self</span>):</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code js-file-line">        <span class="pl-k">return</span> <span class="pl-s3">hash</span>((<span class="pl-v">self</span>.recordType, <span class="pl-v">self</span>.folderID))</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code js-file-line">sCatalogFile <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&#39;</span>CatalogFolder<span class="pl-pds">&#39;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>recordType<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>flags<span class="pl-pds">&#39;</span></span>, </td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code js-file-line">                                             <span class="pl-s1"><span class="pl-pds">&#39;</span>reserved1<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>fileID<span class="pl-pds">&#39;</span></span>, </td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code js-file-line">                                             <span class="pl-s1"><span class="pl-pds">&#39;</span>createDate<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>contentModDate<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>attributeModDate<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>accessDate<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>backupDate<span class="pl-pds">&#39;</span></span>, </td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code js-file-line">                                             <span class="pl-s1"><span class="pl-pds">&#39;</span>permissions<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>userInfo<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>finderInfo<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code js-file-line">                                             <span class="pl-s1"><span class="pl-pds">&#39;</span>textEncoding<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>reserved2<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code js-file-line">                                             <span class="pl-s1"><span class="pl-pds">&#39;</span>dataFork<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>resourceFork<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code js-file-line"><span class="pl-st">class</span> <span class="pl-en">CatalogFile</span>(<span class="pl-e">sCatalogFile</span>):</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code js-file-line">    <span class="pl-sv">__slots__</span> <span class="pl-k">=</span> ()</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__len__</span></span>(<span class="pl-vpf">self</span>):</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">248</span></td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__eq__</span></span>(<span class="pl-vpf">self</span>, <span class="pl-vpf">other</span>):</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code js-file-line">        <span class="pl-k">return</span> ((<span class="pl-v">self</span>.recordType <span class="pl-k">==</span> other.recordType) <span class="pl-k">and</span> (<span class="pl-v">self</span>.fileID <span class="pl-k">==</span> other.fileID))</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__hash__</span></span>(<span class="pl-vpf">self</span>):</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code js-file-line">        <span class="pl-k">return</span> <span class="pl-s3">hash</span>((<span class="pl-v">self</span>.recordType, <span class="pl-v">self</span>.fileID))</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code js-file-line"><span class="pl-st">class</span> <span class="pl-en">CatalogThread</span>(<span class="pl-e">namedtuple(<span class="pl-s1"><span class="pl-pds">&quot;</span>CatalogThread<span class="pl-pds">&quot;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>recordType<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>reserved<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>parentID<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>nodeName<span class="pl-pds">&#39;</span></span>])</span>):</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code js-file-line">    <span class="pl-sv">__slots__</span> <span class="pl-k">=</span> ()</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__len__</span></span>(<span class="pl-vpf">self</span>):</td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">8</span><span class="pl-k">+</span><span class="pl-c1">2</span><span class="pl-k">+</span><span class="pl-c1">2</span><span class="pl-k">*</span><span class="pl-v">self</span>.nodeName[<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__eq__</span></span>(<span class="pl-vpf">self</span>, <span class="pl-vpf">other</span>):</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code js-file-line">        <span class="pl-k">return</span> ((<span class="pl-v">self</span>.recordType <span class="pl-k">==</span> other.recordType) <span class="pl-k">and</span> (<span class="pl-v">self</span>.nodeName <span class="pl-k">==</span> other.nodeName))</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__hash__</span></span>(<span class="pl-vpf">self</span>):</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code js-file-line">        <span class="pl-k">return</span> <span class="pl-s3">hash</span>((<span class="pl-v">self</span>.recordType, <span class="pl-v">self</span>.nodeName))</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code js-file-line"><span class="pl-c"># User data structure</span></td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code js-file-line">CatalogLeaf <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&quot;</span>CatalogLeaf<span class="pl-pds">&quot;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>NodeDescriptor<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>LeafRecList<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code js-file-line">CatalogHeader <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&quot;</span>CatalogHeader<span class="pl-pds">&quot;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>NodeDescriptor<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>BTHeaderRec<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>UserDataRec<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>MapRec<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code js-file-line"><span class="pl-st">class</span> <span class="pl-en">UniChar</span>(<span class="pl-e">namedtuple(<span class="pl-s1"><span class="pl-pds">&quot;</span>UniChar<span class="pl-pds">&quot;</span></span>, [<span class="pl-s1"><span class="pl-pds">&#39;</span>nameLen<span class="pl-pds">&#39;</span></span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>nodeUnicode<span class="pl-pds">&#39;</span></span>])</span>):</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code js-file-line">    <span class="pl-sv">__slots__</span> <span class="pl-k">=</span> ()</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code js-file-line">    </td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code js-file-line">    <span class="pl-st">def</span> <span class="pl-en"><span class="pl-s3">__eq__</span></span>(<span class="pl-vpf">self</span>, <span class="pl-vpf">other</span>):</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code js-file-line">        lenComp <span class="pl-k">=</span> (<span class="pl-v">self</span>.nameLen <span class="pl-k">==</span> other.nameLen)</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code js-file-line">        nameComp <span class="pl-k">=</span> (<span class="pl-v">self</span>.nodeUnicode <span class="pl-k">==</span> other.nodeUnicode)</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code js-file-line">        <span class="pl-k">return</span> (lenComp <span class="pl-k">and</span> nameComp)</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code js-file-line">BTPointerRec <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&#39;</span>BTPointerRec<span class="pl-pds">&#39;</span></span>, BTKey._fields<span class="pl-k">+</span>(<span class="pl-s1"><span class="pl-pds">&#39;</span>nodeNumber<span class="pl-pds">&#39;</span></span>,))</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code js-file-line">ExtentKey <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&#39;</span>ExtentKey<span class="pl-pds">&#39;</span></span>,BTKey._fields<span class="pl-k">+</span>(<span class="pl-s1"><span class="pl-pds">&#39;</span>forkType<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>pad<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>fileID<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>startBlock<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code js-file-line">ExtentsDataRec <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&#39;</span>ExtentsDataRec<span class="pl-pds">&#39;</span></span>,ExtentKey._fields<span class="pl-k">+</span>(<span class="pl-s1"><span class="pl-pds">&#39;</span>extents<span class="pl-pds">&#39;</span></span>,))</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code js-file-line">AttrKey <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&#39;</span>AttrKey<span class="pl-pds">&#39;</span></span>,BTKey._fields<span class="pl-k">+</span>(<span class="pl-s1"><span class="pl-pds">&#39;</span>pad<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>fileID<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>startBlock<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>attrNameLen<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>attrName<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>recordType<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>reserved<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code js-file-line">AttrForkData <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&#39;</span>AttrForkData<span class="pl-pds">&#39;</span></span>,AttrKey._fields<span class="pl-k">+</span>(<span class="pl-s1"><span class="pl-pds">&#39;</span>theFork<span class="pl-pds">&#39;</span></span>,))</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code js-file-line">AttrExtents <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&#39;</span>AttrExtents<span class="pl-pds">&#39;</span></span>,AttrKey._fields<span class="pl-k">+</span>(<span class="pl-s1"><span class="pl-pds">&#39;</span>extents<span class="pl-pds">&#39;</span></span>,))</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code js-file-line">AttrData <span class="pl-k">=</span> namedtuple(<span class="pl-s1"><span class="pl-pds">&#39;</span>AttrData<span class="pl-pds">&#39;</span></span>,AttrKey._fields<span class="pl-k">+</span>(<span class="pl-s1"><span class="pl-pds">&#39;</span>reserved2<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>attrSize<span class="pl-pds">&#39;</span></span>,<span class="pl-s1"><span class="pl-pds">&#39;</span>attrData<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code js-file-line">
</td>
      </tr>
</table>

  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="https://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.06968s from github-fe134-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder=""></textarea>
      <div class="suggester-container">
        <div class="suggester fullscreen-suggester js-suggester js-navigation-container"></div>
      </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-996268c2962f947579cb9ec2908bd576591bc94b6a2db184a78e78815022ba2c.js"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-a7bddfcfdd35f67bb7fe4fcd1c4fb64f6b3dad6d75980b243af9e7ad1f55035f.js"></script>
      
      

  </body>
</html>

