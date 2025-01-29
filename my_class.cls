\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{my_class}[My custom class]

\LoadClass{article}

\RequirePackage{hyperref}
\RequirePackage{import}
\RequirePackage{mathptmx}
\RequirePackage{xcolor}
\RequirePackage{tikz}
\RequirePackage{lipsum}
\usetikzlibrary{mindmap,trees}
\RequirePackage{verbatim}
\RequirePackage{geometry}


\hypersetup{
    colorlinks = true,
    linkcolor = red,
    linkbordercolor = {white}
}

%\titleformat{\section}         % Customise the \section command 
%  {\Large\scshape\raggedright} % Make the \section headers large (\Large),
                               % small capitals (\scshape) and left aligned (\raggedright)
%  {}{0em}                      % Can be used to give a prefix to all sections, like 'Section ...'
%  {}                           % Can be used to insert code before the heading
%  [\titlerule]                 % Inserts a horizontal line after the heading


%\newcommand{\datedsection}[2]{%
%  \section[#1]{#1 \hfill #2}

%\label{sec:hello}
%to do a hyperref to section
%\hyperref[sec:hello]{Word of text}

\newlength\tindent
\setlength{\tindent}{\parindent}
\setlength{\parindent}{0pt}
\renewcommand{\indent}{\hspace*{\tindent}}

\geometry{
  paper=a4paper,
  margin=90pt
}

\import{./Commands/}{commands.tex}

%CONSTANTS

\newcommand{\contentstitle}{Contents}