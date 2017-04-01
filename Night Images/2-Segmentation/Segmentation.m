function varargout = Segmentation(varargin)
% SEGMENTATION MATLAB code for Segmentation.fig
%      SEGMENTATION, by itself, creates a new SEGMENTATION or raises the existing
%      singleton*.
%
%      H = SEGMENTATION returns the handle to a new SEGMENTATION or the handle to
%      the existing singleton*.
%
%      SEGMENTATION('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in SEGMENTATION.M with the given input arguments.
%
%      SEGMENTATION('Property','Value',...) creates a new SEGMENTATION or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Segmentation_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Segmentation_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help Segmentation

% Last Modified by GUIDE v2.5 22-Jan-2014 18:15:44

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @Segmentation_OpeningFcn, ...
                   'gui_OutputFcn',  @Segmentation_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before Segmentation is made visible.
function Segmentation_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to Segmentation (see VARARGIN)

% Choose default command line output for Segmentation
handles.output = hObject;

% Initial setup
dispBorders = true;
dispLabels = true;
divideBy = 50;
compactness = 10;
applyLabelChange = false;
selectedLabel = 1;

set(handles.dispBorders, 'Value', dispBorders);
set(handles.dispLabels, 'Value', dispLabels);
set(handles.divideBy, 'String', divideBy);
set(handles.compactness, 'Value', log10(compactness));
set(handles.compactness_text, 'String', '-     Compactness (10)     +');
set(handles.modifyLabels, 'Value', applyLabelChange);

% Apply the selected label value
switch selectedLabel
    case 0
        set(handles.labelRemove, 'Value', 1.0);
    case 1
        set(handles.labelClear, 'Value', 1.0);
    case 2
        set(handles.labelPuffy, 'Value', 1.0);
    case 3
        set(handles.labelThick, 'Value', 1.0);
    case 4
        set(handles.labelThin, 'Value', 1.0);
    case 5
        set(handles.labelVeil, 'Value', 1.0);
    case 42
        set(handles.labelSpec, 'Value', 1.0);
    case 43
        set(handles.labelOccl, 'Value', 1.0);
end

%%%%%%%%%%%%%%%% MODIFY IMAGE INDEX HERE %%%%%%%%%%%%%%%%
prompt = {'Enter image number:'};
dlg_title = 'Image number';
num_lines = 1;
def = {'1'};
imageName = inputdlg(prompt,dlg_title,num_lines,def);
imageName = imageName{1};
% imageName = input('Enter image name: ', 's');
image = imread(['images/', imageName, 'img.png']);
if exist(['images/', imageName, 'segm.png'], 'file') == 2
    initSegm = imread(['images/', imageName, 'segm.png']);
    if size(initSegm, 3) == 3
        initSegm = rgb2gray(initSegm);
    end
    initSegm = round(im2double(initSegm));
else
    initSegm = NaN;
end
            
handles.computation = currentComputation(image, divideBy, compactness, ...
    dispBorders, dispLabels, applyLabelChange, selectedLabel, initSegm, imageName);

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes Segmentation wait for user response (see UIRESUME)
% uiwait(handles.figure1);

% --- Outputs from this function are returned to the command line.
function varargout = Segmentation_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on button press in radiobutton5.
function radiobutton5_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton5


% --- Executes on button press in radiobutton6.
function radiobutton6_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton6 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton6


% --- Executes on button press in undo.
function undo_Callback(hObject, eventdata, handles)
% hObject    handle to undo (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
computation = handles.computation;

computation.currentSegmInd = computation.currentSegmInd - 1;
computation.displayImage;

handles.computation = computation;
set(handles.redo, 'Enable', 'On');
if computation.currentSegmInd == 1
    set(handles.undo, 'Enable', 'Off');
end

guidata(hObject, handles);


% --- Executes on button press in redo.
function redo_Callback(hObject, eventdata, handles)
% hObject    handle to redo (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
computation = handles.computation;

computation.currentSegmInd = computation.currentSegmInd + 1;
computation.displayImage;

handles.computation = computation;
set(handles.undo, 'Enable', 'On');
if computation.currentSegmInd == size(computation.segmentations, 3);
    set(handles.redo, 'Enable', 'Off');
end

guidata(hObject, handles);


% --- Executes on button press in modifyLabels.
function modifyLabels_Callback(hObject, eventdata, handles)
% hObject    handle to modifyLabels (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
currentValue = get(hObject, 'Value');
computation = handles.computation;

computation.applyLabelChange = currentValue;

handles.computation = computation;

guidata(hObject, handles);



% --- Executes on button press in dispBorders.
function dispBorders_Callback(hObject, eventdata, handles)
% hObject    handle to dispBorders (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of dispBorders
currentValue = get(hObject, 'Value');
computation = handles.computation;

computation.dispBorders = currentValue;
computation.displayImage;

handles.computation = computation;

guidata(hObject, handles);


% --- Executes on button press in dispLabels.
function dispLabels_Callback(hObject, eventdata, handles)
% hObject    handle to dispLabels (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of dispLabels
currentValue = get(hObject, 'Value');
computation = handles.computation;

computation.dispLabels = currentValue;
computation.displayImage;

handles.computation = computation;

guidata(hObject, handles);

% --- Executes on button press in applyWholeImage.
function applyWholeImage_Callback(hObject, eventdata, handles)
% hObject    handle to applyWholeImage (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

computation = handles.computation;

% We first update divideBy and compactness values
computation.divideBy = str2double(get(handles.divideBy,'String'));
computation.compactness = 10^get(handles.compactness, 'Value');

computation.newSegmentationWholeImage;

handles.computation = computation;
set(handles.undo, 'Enable', 'On');
set(handles.redo, 'Enable', 'Off');

guidata(hObject, handles);


% --- Executes on button press in applySelectedPix.
function applySelectedPix_Callback(hObject, eventdata, handles)
% hObject    handle to applySelectedPix (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

computation = handles.computation;

% We first update divideBy value
computation.divideBy = str2double(get(handles.divideBy,'String'));
computation.compactness = 10^get(handles.compactness, 'Value');

computation.subsegmentSuperpixel;

handles.computation = computation;
set(handles.undo, 'Enable', 'On');
set(handles.redo, 'Enable', 'Off');

guidata(hObject, handles);


function divideBy_Callback(hObject, eventdata, handles)
% hObject    handle to divideBy (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of divideBy as text
%        str2double(get(hObject,'String')) returns contents of divideBy as a double


% --- Executes during object creation, after setting all properties.
function divideBy_CreateFcn(hObject, eventdata, handles)
% hObject    handle to divideBy (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in guessLabels.
function guessLabels_Callback(hObject, eventdata, handles)
% hObject    handle to guessLabels (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

computation = handles.computation;

computation.guessLabels;
handles.computation = computation;

set(handles.undo, 'Enable', 'On');
set(handles.redo, 'Enable', 'Off');

guidata(hObject, handles);


% --- Executes when selected object is changed in modifyLabelPanel.
function modifyLabelPanel_SelectionChangeFcn(hObject, eventdata, handles)
% hObject    handle to the selected object in modifyLabelPanel 
% eventdata  structure with the following fields (see UIBUTTONGROUP)
%	EventName: string 'SelectionChanged' (read only)
%	OldValue: handle of the previously selected object or empty if none was selected
%	NewValue: handle of the currently selected object
% handles    structure with handles and user data (see GUIDATA)

computation = handles.computation;

switch get(hObject, 'Tag')
    case 'labelClear'
        computation.selectedLabel = 1;
    case 'labelPuffy'
        computation.selectedLabel = 2;
    case 'labelThick'
        computation.selectedLabel = 3;
    case 'labelThin'
        computation.selectedLabel = 4;
    case 'labelVeil'
        computation.selectedLabel = 5;
    case 'labelSpec'
        computation.selectedLabel = 42;
    case 'labelOccl'
        computation.selectedLabel = 43;
    case 'labelRemove'
        computation.selectedLabel = 0;
end

guidata(hObject, handles);


% --- Executes on slider movement.
function compactness_Callback(hObject, eventdata, handles)
% hObject    handle to compactness (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'Value') returns position of slider
%        get(hObject,'Min') and get(hObject,'Max') to determine range of slider

val = get(hObject, 'Value');
set(handles.compactness_text, 'String', ['-     Compactness (', num2str(10^val),')     +']);


% --- Executes during object creation, after setting all properties.
function compactness_CreateFcn(hObject, eventdata, handles)
% hObject    handle to compactness (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: slider controls usually have a light gray background.
if isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor',[.9 .9 .9]);
end


% --- Executes on button press in save.
function save_Callback(hObject, eventdata, handles)
% hObject    handle to save (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

computation = handles.computation;

computation.save();

handles.computation = computation;

guidata(hObject, handles);
